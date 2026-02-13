@app.route("/book", methods=["POST"])
def book():
    # Try reading JSON
    payload = request.get_json(silent=True)

    # If Ringg sent form-data instead
    if not payload:
        payload = request.form.to_dict()

    # Forward as JSON to backend
    res = requests.post(
        "https://utkarshshukla2912.pythonanywhere.com/api/v1/appointments",
        json=payload
    )

    return jsonify(res.json()), res.status_code

