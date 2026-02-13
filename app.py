from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "online"}

@app.route("/book", methods=["POST"])
def book():
    payload = request.get_json(silent=True)

    if not payload:
        payload = request.form.to_dict()

    res = requests.post(
        "https://utkarshshukla2912.pythonanywhere.com/api/v1/appointments",
        json=payload
    )

    return jsonify(res.json()), res.status_code


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
