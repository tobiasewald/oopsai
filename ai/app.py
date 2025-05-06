from fastapi import FastAPI, File, UploadFile
import uvicorn, json

app = FastAPI()

@app.post("/analyze")
async def analyze(trivy: UploadFile = File(...), owasp: UploadFile = File(...)):
    trivy_data = json.load(trivy.file)
    owasp_data = json.load(owasp.file)
    
    critical_issues = len([x for x in trivy_data.get("Results", []) if x.get("Severity") == "CRITICAL"])
    comment = "🔥 Oops! Critical issues found." if critical_issues > 0 else "✅ All good, mostly."
    
    return {
        "summary": f"Found {critical_issues} critical issues.",
        "comment": comment,
        "meme": "https://i.imgflip.com/5h0z.jpg"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)