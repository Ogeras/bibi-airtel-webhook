from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def airtel_webhook():
    data = request.json
    print("Received data:", data)

    # You can add logic here to send download link after successful payment
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run()
