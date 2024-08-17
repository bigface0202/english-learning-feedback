from flask import Flask, request, jsonify

from src.driver import bootstrap

app = Flask(__name__)

conv_svc, trns_svc = bootstrap()

@app.route("/conversation", methods = ["POST"])
def conversation():
    data:object = request.get_json()
    gcs_uri:str = data.get('gcs_uri')
    message = trns_svc.make_transcription(gcs_uri)
    reply = conv_svc.make_reply(message)
    print(f"message: {message}")
    print(f"reply: {reply}")

    response = {
        "message": message,
        "reply": reply
    }

    return jsonify(response), 200

@app.route("/")
def read_root():
    return {"message": "Health Check OK"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080)
