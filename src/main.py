from flask import Flask, jsonify

from src.driver import bootstrap

app = Flask(__name__)

conv_svc, trns_svc = bootstrap()

@app.route("/conversation", methods = ["POST"])
def conversation():
    #TODO: Extract human message from POST request
    message = trns_svc.make_transcription("gs://cloud-samples-data/speech/brooklyn_bridge.raw")
    reply = conv_svc.make_reply(message)
    print(f"message: {message}")
    print(f"reply: {reply}")

    response = {
        "message": message,
        "reply": reply
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080)
