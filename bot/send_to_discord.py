import sys, json, requests

with open(sys.argv[1], "r") as f:
    data = json.load(f)

webhook_url = "https://discord.com/api/webhooks/1369239770181533739/mXcFlcWTjenDosH7LT6KlZJr1fL5bgVDERynyB0vOmxi9DpyQtO6YqvTJu7XusY8OWzj"

payload = {
    "content": f"**Oops.ai Scan Ergebnis:**\n{data['summary']}\n\n{data['comment']}",
    "embeds": [
        {"image": {"url": data["meme"]}}
    ]
}

requests.post(webhook_url, json=payload)