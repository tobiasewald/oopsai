# Ollama API Wrapper für die HTW Berlin

Dieses Repository enthält eine Python-Klasse (`OllamaApi`), mit der ihr über das interne Netzwerk der HTW Berlin Anfragen an den Ollama-Dienst senden könnt. Die Nutzung setzt eine aktive VPN-Verbindung voraus.

## 🔌 Voraussetzungen

- Python 3.7 oder neuer
- VPN-Zugang zur HTW Berlin
- Zugriff auf:  
  `https://f2ki-h100-1.f2.htw-berlin.de:11435`

## 📦 Installation

```python
pip install requests
```

## 🧠 Unterstützte Funktionen

- Modelle auflisten
- Text-Vervollständigung (Prompt)
- Chat-Konversation mit Rollen
- Unterstützung für strukturierte JSON-Antworten
- Robuste Fehlerbehandlung

## 🚀 Verwendung

```python
from examples import OllamaApi
```

### Text Completion

```python
result = OllamaApi.completion("Schreibe ein Haiku über den Frühling.")
print(result)
```

### Chat

```python
chat = [
    {"role": "system", "content": "Du bist ein Haiku-Meister"},
    {"role": "user", "content": "Ein Haiku über Herbst"}
]
chat_result = OllamaApi.chat(chat)
print(chat_result)
```

### Completion mit JSON-Schema

```python
schema = {
    "type": "object",
    "properties": {
        "lines": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["lines"]
}
json_result = OllamaApi.completion("Schreibe ein Haiku über den Winter", schema=schema)
print(json_result)
```

## 🛠 Methodenübersicht

| Methode                 | Beschreibung                                          |
|-------------------------|-------------------------------------------------------|
| `models()`              | Gibt installierte Modelle auf dem Server zurück       |
| `completion()`          | Führt eine Prompt-Vervollständigung aus               |
| `chat()`                | Führt einen Dialog mit mehreren Rollen                |
| `api_request()`         | Interne Hilfsmethode für Completion/Chat              |
| `secure_json_response()`| Filtert und parsed JSON-Daten sicher                  |
| `secure_text_response()`| Gibt Textantworten formatiert zurück                  |

## 🧪 Beispiele

Die Datei `examples.py` enthält vier durchführbare Beispiele, inklusive:

1. Text Completion
2. Chat mit Rollen
3. JSON-Strukturierte Completion
4. JSON-Strukturierter Chat

Ausführen mit:

```python
python examples.py
```
