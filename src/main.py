from flask import Flask, request, jsonify

from src.driver import bootstrap

app = Flask(__name__)

conv_svc, trn_svc = bootstrap()

@app.route("/conversation", methods = ["POST"])
def conversation():
    data:object = request.get_json()
    human_message:str = data.get('human_message')
    reply = conv_svc.make_reply(human_message)
    print(f"message: {human_message}")
    print(f"reply: {reply}")

    response = {
        "message": human_message,
        "reply": reply
    }

    return jsonify(response), 200

@app.route("/audio", methods = ["POST"])
def audio():
    data:object = request.get_json()
    gcs_uri:str = data.get('gcs_uri')
    trn_svc.transcribe(gcs_uri)

    return {"message": "Audio is transcribed"}, 200

@app.route("/")
def read_root():
    return {"message": "Health Check OK"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080)
