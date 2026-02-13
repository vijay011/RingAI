from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

BACKEND = "https://utkarshshukla2912.pythonanywhere.com/api/v1/appointments"

@app.route("/")
def home():
    return {"status": "online"}

@app.route("/book", methods=["POST"])
def book():
    # Try JSON first
    data = request.get_json(silent=True)

    # If Ringg sent form-data instead
    if not data:
        data = request.form.to_dict()

    # Clean payload (very important)
    cleaned = {}
    for k, v in data.items():
        if v is None:
            continue
        value = str(v).strip()
        if value != "":
            cleaned[k] = value

    # Forward to backend as JSON
    res = requests.post(BACKEND, json=cleaned)

    return (res.text, res.status_code, {'Content-Type':'application/json'})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
