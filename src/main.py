from flask import Flask

from src.driver import bootstrap

app = Flask(__name__)

svc = bootstrap()

@app.route("/conversation", methods = ["POST"])
def conversation():
    #TODO: Extract human message from POST request
    message = """
        I'm Yusuke, and living in Tokyo, and working as IT engineer at the company.
        In my free time, I like to go to gym to workout, watching Netfilx, go hiking, and playing video game.
        Thank you, and nice to meet you.
        """
    reply = svc.make_reply(message)
    print(f"message: {message}")
    print(f"reply: {reply}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080)
