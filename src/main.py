from flask import Flask, request, jsonify
from flask_cors import CORS

from src.driver import bootstrap

app = Flask(__name__)
CORS(app)

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
    gcs_uri:str = data.get("gcs_uri")
    user_uid:str = data.get("user_uid")
    lesson_date:str = data.get("lesson_date")
    note:str = data.get("note")

    trn_svc.transcribe(
        gcs_uri = gcs_uri,
        user_uid = user_uid,
        lesson_date = lesson_date,
        note = note,
    )

    return {"message": "Audio is transcribed"}, 200

@app.route("/")
def read_root():
    return {"message": "Health Check OK"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080)
