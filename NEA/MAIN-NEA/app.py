from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cust")
def cust():
    return render_template("customer.html")

@app.route("/hair")
def hair():
    return render_template("hairdresser.html")

@app.route("/log")
def log():
    return render_template("Login.html")

@app.route("/shce")
def shced():
    return render_template("shcedule.html")

if __name__ == "__main__":
    app.run()