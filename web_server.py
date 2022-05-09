from flask import Flask, render_template, Response
from generate_video_stream import generate_stream

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_stream")
def video_stream():
    return render_template("video_stream.html")

@app.route("/video_feed_stream")
def video_feed_stream():
    return Response(generate_stream(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    # app.run(host="192.168.1.103", port=5001)
    app.run(host="192.168.157.1", port=5001)
