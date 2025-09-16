from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import uuid
import requests

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
SUPABASE_TABLE = os.getenv("SUPABASE_TABLE")

HEADERS = {
    'apikey': SUPABASE_API_KEY,
    'Authorization': f'Bearer {SUPABASE_API_KEY}',
    'Content-Type': 'application/json'
}


@app.route("/api/save_qr_data", methods=["POST"])
def save_qr_data():
    data = request.json

    required_fields = [
        "partType", "serialNo", "vendorId", "mfgDate", "lotNo", "warrantyPeriod"
    ]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Generate UID (used as 'id' in Supabase)
    uid = str(uuid.uuid4())

    # Map frontend field names to Supabase column names
    payload = {
        "id": uid,
        "part_type": data["partType"],
        "serial_no": data["serialNo"],
        "vendor_id": data["vendorId"],
        "mfg_date": data["mfgDate"],
        "lot_no": data["lotNo"],
        "warranty_period": data["warrantyPeriod"]
        # time_stamp is auto-filled
    }

    # POST to Supabase
    res = requests.post(f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}", headers=HEADERS, json=payload)

    if res.status_code in [200, 201]:
        return jsonify({"uid": uid}), 201
    else:
        return jsonify({
            "error": "Failed to store data in Supabase",
            "details": res.text
        }), 500


@app.route("/showdata/<uid>", methods=["GET"])
def get_qr_data(uid):
    query_url = f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?id=eq.{uid}"

    res = requests.get(query_url, headers=HEADERS)

    if res.status_code == 200:
        data = res.json()
        if data:
            return render_template("show_data.html", data=data[0])
        else:
            return jsonify({"error": "UID not found"}), 404
    else:
        return jsonify({"error": "Failed to fetch data", "details": res.text}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
