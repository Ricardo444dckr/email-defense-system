from analyzer.text_check import analyze_text

email_text = "URGENTE! Clique aqui para verificar sua conta agora."

score, reasons = analyze_text(email_text)

print("Score:", score)
print("Motivos:")
for r in reasons:
    print("-", r)