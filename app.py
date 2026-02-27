# from flask import Flask
# app = Flask(__name__)

# @app.route("/") #This is a decorator. It tells Flask that whenever someone visits the "root" URL (the / at the end o
# #f your domain, like http://localhost:5000/), it should run the function directly below it.
# def home():
#     return "Hello DevOps! 🚀"

# if __name__ == "__main__":
#     #if __name__ == "__main__":: This ensures the server only starts if you run this specific file directly (not if you import it elsewhere).
#     app.run(host="0.0.0.0", port=5000)
#     #host="0.0.0.0": This is a crucial DevOps detail. By default, Flask only listens on 127.0.0.1 (your local machine). Setting it to 0.0.0.0 tells the app to listen on all available network interfaces. This is 
#     # usually required to access the app from inside a Docker container or over a network.\
#     #port=5000: This sets the specific "door" the app listens on.
from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "Default App")
    return f"{app_name} 🚀 Running on {socket.gethostname()}"
@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)