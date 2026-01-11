from analyzer.link_check import analyze_links

email_body = "Acesse https://bit.ly/pega-voucher ou http://incrivel.super.seguro.domain.com.br agora!"

score, reasons = analyze_links(email_body)

print("Score:", score)
print("Motivos:")
for r in reasons:
    print("-", r)