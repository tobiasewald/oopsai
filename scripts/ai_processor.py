import json
from htw_ollama_api.examples import OllamaApi


def analyze_security(trivy_data, owasp_data):
    prompt = f"""
Analysiere die folgenden Sicherheitsberichte:

TRIVY Report:
{json.dumps(trivy_data)}

OWASP Dependency Check Report:
{json.dumps(owasp_data)}

Gib ein JSON zurück wie folgt (keine Erklärung, kein Text drumherum):

{{
  "criticality": <Zahl von 0 bis 10>,
  "comment": "<kurze Einschätzung auf Deutsch>"
}}
"""
    response = OllamaApi.completion(
        prompt=prompt,
        model="codellama:instruct",  # oder dein Modellname (z. B. llama3.3:70b)
        schema={
            "type": "object",
            "properties": {
                "criticality": { "type": "number" },
                "comment": { "type": "string" }
            },
            "required": ["criticality", "comment"]
        }
    )

    return response.get("result")


def generate_meme(criticality):
    prompt = f"""
Du bist SentinelAI – ein zynischer DevOps-Agent.
Schreibe einen einzigen sarkastischen Satz über eine Sicherheitskritikalität von {criticality}/10.
Kein Emoji, keine Einleitung, keine Erklärung. Nur der Satz.
"""
    response = OllamaApi.completion(
        prompt=prompt,
        model="llama3",  # oder llama3.3:70b – je nachdem, was installiert ist
    )

    return response.get("result")


def main():
    try:
        with open("trivy-report.json") as f1, open("dependency-check-report.json") as f2:
            trivy = json.load(f1)
            owasp = json.load(f2)
    except Exception as e:
        print(f"Fehler beim Laden der Reports: {e}")
        return

    try:
        analysis = analyze_security(trivy, owasp)
        with open("ai_response.json", "w", encoding="utf-8") as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)
        print("✅ Analyse gespeichert.")
    except Exception as e:
        print(f"Fehler bei Analyse: {e}")
        analysis = {"criticality": 10, "comment": "Standardwert wegen Fehler"}

    try:
        meme = generate_meme(analysis["criticality"])
        with open("ai_meme.json", "w", encoding="utf-8") as f:
            json.dump({"meme": meme}, f, indent=2, ensure_ascii=False)
        print("✅ Meme gespeichert.")
    except Exception as e:
        print(f"Fehler bei Meme-Generierung: {e}")


if __name__ == "__main__":
    main()
