#import json
from flask import Flask, render_template, request, json,Response
from jpg_func import search_and_down
import pymongo
conn_str = "mongodb://localhost:5000"
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/result", methods=['POST', "GET"])
def result():
    if request.method == 'POST':
        output = request.form.to_dict()
        name = output["name"]
        return f'<img src="{search_and_down(name)}">'

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

