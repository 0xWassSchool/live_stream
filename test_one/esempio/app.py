from flask import Flask, Response, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/video")
def video():
    return Response(camera_video() ,mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run()
