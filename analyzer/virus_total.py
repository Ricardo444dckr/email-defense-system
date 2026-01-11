import os
import requests
from dotenv import load_dotenv

# carregar a variável de ambiente com tua chave
load_dotenv()
VT_API_KEY = os.getenv("VT_API_KEY")

def check_url(url: str):
    """Verifica um link no VirusTotal"""
    try:
        headers = {"x-apikey": VT_API_KEY}
        scan_url = "https://www.virustotal.com/api/v3/urls"

        # enviar o URL para análise
        res = requests.post(scan_url, data={"url": url}, headers=headers)
        if res.status_code != 200:
            return False, f"Erro ao enviar URL ({res.status_code})"

        url_id = res.json()["data"]["id"]
        analysis_url = f"{scan_url}/{url_id}"
        analysis_res = requests.get(analysis_url, headers=headers).json()

        malicious = analysis_res["data"]["attributes"]["stats"]["malicious"]
        if malicious > 0:
            return True, f"Detetado como malicioso ({malicious} motores)."
        return False, "Limpo segundo VirusTotal."

    except Exception as e:
        return False, f"Erro: {e}"