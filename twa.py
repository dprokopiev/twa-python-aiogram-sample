from flask import Flask, render_template, request, redirect
from os import listdir

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/photos")
def photos():
    images = listdir("static/img/")

    return render_template("photos.html", images=images)

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        files = request.files

        if "image" not in files:
            return render_template("send.html")

        image = request.files["image"]
        filename = image.filename
        image.save(f"static/img/{filename}")

        return redirect("/photos")

    return render_template("send.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000, debug=True)