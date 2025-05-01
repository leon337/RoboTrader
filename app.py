from flask import Flask, render_template, send_file
from iq_bot import login_and_capture

app = Flask(__name__)

@app.route("/")
def home():
    screenshot_path = login_and_capture()
    return render_template("index.html", screenshot="screenshot.png")

@app.route("/screenshot.png")
def screenshot():
    return send_file("static/screenshot.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
