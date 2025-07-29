from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload-key', methods=['POST'])
def upload_key():
    data = request.json
    key = data.get('key')   # base64 encoded key
    iv = data.get('iv')     # base64 encoded IV

    print("Key:", key)
    print("IV :", iv)

    return jsonify({"message": "Key received successfully"}), 200

if __name__ == '__main__':
    # Ye HTTPS mode mein chalega (SSL certificate ke saath)
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))


