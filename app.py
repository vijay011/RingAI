from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Original backend booking API
BACKEND = "https://utkarshshukla2912.pythonanywhere.com/api/v1/appointments"


@app.route("/")
def home():
    return {"status": "online", "service": "Ringg Booking Adapter"}


@app.route("/book", methods=["POST"])
def book():
    try:
        # Try JSON first (Ringg sometimes sends JSON)
        data = request.get_json(silent=True)

        # If empty, read form-data
        if not data:
            data = request.form.to_dict()

        # Clean payload
        cleaned = {}
        for k, v in data.items():
            if v is None:
                continue
            value = str(v).strip()
            if value != "":
                cleaned[k] = value

        # Forward to backend as JSON
        res = requests.post(BACKEND, json=cleaned)

        # Return proper JSON response (important for Ringg)
        return jsonify(res.json()), res.status_code

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
