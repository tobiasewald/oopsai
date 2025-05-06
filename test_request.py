import requests
import json

files = {
    'trivy': open('trivy_report.json', 'rb'),
    'owasp': open('trivy_report.json', 'rb')  # Nur zu Testzwecken
}

response = requests.post("http://localhost:8000/analyze", files=files)

print("Status:", response.status_code)
print("Antwort:")
print(response.json())

# Speichere die Antwort als ai_response.json
with open("ai_response.json", "w") as f:
    json.dump(response.json(), f, indent=2)
