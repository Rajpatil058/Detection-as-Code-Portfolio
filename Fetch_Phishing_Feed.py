import requests
import json

# The Target: Feodo Tracker (Active Botnet C2 IPs - No API Key Required)
FEED_URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.json"

def fetch_and_parse_iocs():
    print("[*] Fetching active Botnet C2 IPs from Feodo Tracker...")
    
    try:
        # The Bypass: We spoof the User-Agent so the API doesn't block us as a generic Python bot
        headers = {'User-Agent': 'Mozilla/5.0 (DetectionEngineering-Portfolio)'}
        
        response = requests.get(FEED_URL, headers=headers)
        response.raise_for_status() # Check if the connection was successful
        
        # Parse the JSON data
        raw_data = response.json()
        
        # Extract the first 20 Botnet IPs
        malicious_ips = []
        for entry in raw_data[:20]:
            ip = entry.get('ip_address')
            if ip:
                malicious_ips.append(ip)
                
        # Save the clean data to a text file
        with open("parsed_iocs.txt", "w") as file:
            for ip in malicious_ips:
                file.write(f"{ip}\n")
                
        print(f"[+] Success! Saved {len(malicious_ips)} Botnet IPs to parsed_iocs.txt")

    except Exception as e:
        print(f"[-] Automated pipeline failed: {e}")

# Run the function
if __name__ == "__main__":
    fetch_and_parse_iocs()