from flask import Flask, render_template, request, redirect

app = Flask(__name__)

counts=0


@app.route("/request_counter", methods=["GET", "POST"])
def request_counter():
    if request.method=="GET":
        global counts
        counts += 1
        return redirect("/")


@app.route("/")
def index():
    return render_template("index.html", counts=counts)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True,
    )
