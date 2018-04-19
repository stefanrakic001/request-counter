from flask import Flask, render_template, request, redirect

app = Flask(__name__)

counts= {"GET":0, "POST":0, "DELETE":0, "PUT":0}


@app.route("/request_counter", methods=["GET", "POST", "DELETE", "PUT"])
def request_counter():
    if request.method in ["GET", "POST", "DELETE", "PUT"]:
        global counts
        counts[request.method] += 1
        return redirect("/")


# @app.route("/statistic")
# def statiscitc():


@app.route("/")
def index():
    return render_template("index.html", counter=counts)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True,
    )
