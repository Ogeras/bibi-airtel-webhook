from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Bibi Airtel Webhook is Live!', 200

@app.route('/airtel-webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    print("Received Airtel webhook data:", data)

    # TODO: Process the Airtel webhook payload here...

    return jsonify({"message": "Webhook received successfully"}), 200

# Do NOT include app.run(debug=True)