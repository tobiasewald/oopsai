import flask
import requests

app = flask.Flask(__name__)

@app.route("/")
def home():
    # Unsicher: Keine Headerprüfung, keine Timeout-Angabe
    r = requests.get("http://example.com")
    return r.text

if __name__ == "__main__":
    app.run(debug=True)
