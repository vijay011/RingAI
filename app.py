from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BACKEND = "https://utkarshshukla2912.pythonanywhere.com/api/v1/appointments"

@app.route("/")
def home():
    return {"status": "online"}

@app.route("/book", methods=["POST"])
def book():
    payload = request.form.to_dict()
    res = requests.post(BACKEND, json=payload)
    return jsonify(res.json()), res.status_code
