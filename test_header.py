from analyzer.header_check import analyze_headers

headers = "spf=fail dkim=fail"

score, reasons = analyze_headers(headers)

print("Score:", score)
print("Motivos:")
for r in reasons:
    print("-", r)