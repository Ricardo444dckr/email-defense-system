import pandas as pd
import sqlite3
import streamlit as st

st.set_page_config(page_title="Email Defense Dashboard", layout="wide")
st.title("📊 Email Defense – Histórico de Análises")

try:
    conn = sqlite3.connect("reports/report.db")
    df = pd.read_sql_query("SELECT * FROM analyses ORDER BY date DESC", conn)
    conn.close()
except Exception as e:
    st.error(f"Erro ao ler a base de dados: {e}")
    st.stop()

if df.empty:
    st.info("Nenhuma análise ainda foi registada.")
else:
    col1, col2 = st.columns(2)
    total = len(df)
    maliciosos = df["verdict"].eq("Malicioso").sum()
    percent = round((maliciosos / total) * 100, 1)

    col1.metric("Total Análises", total)
    col2.metric("Maliciosos (%)", percent)

    st.markdown("### 📋 Registos")
    st.dataframe(df, use_container_width=True)

    st.markdown("### 📈 Distribuição de Scores")
    st.bar_chart(df["score"])