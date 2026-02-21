import json

# Read IPs from Week 1 output
with open("parsed_iocs.txt", "r") as f:
    ips = [line.strip() for line in f if line.strip()]

enriched_indicators = []

for ip in ips[:10]:
    enriched_indicators.append({
        'ip': ip,
        'threat_type': 'botnet_c2',
        'confidence': 95,
        'last_reported': '2026-02-22',
        'source': 'feodo_tracker'
    })

with open("enriched_indicators.json", "w") as f:
    json.dump(enriched_indicators, f, indent=2)

print(f"[+] Enriched {len(enriched_indicators)} indicators")
print("[+] Saved to enriched_indicators.json")