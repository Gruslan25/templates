from flask import Flask, render_temolate

app = Flask(__name__)

@app.route("/")
def main()
    return render_temolate('index.html')