import json
import shutil
import requests
from datetime import datetime
import pymongo
from flask import Flask, render_template, request, jsonify
from functions.pymongo_intr import down_req
from functions.jpg_func import search_and_down
from pymongo import MongoClient


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://db_host:27017"
#CONNECTION_STRING = "mongodb+srv://basbusa:16456145@cluster0.jvols.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient("mongodb://db_host:27017")

db = db = client.get_database('Moviesproject')
user_collection = pymongo.collection.Collection(db, 'Posters')
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/result", methods=['POST', "GET"])
def result():
    if request.method == 'POST':
        output = request.form.to_dict()
        global name
        name = output["mvname"]
        global resultmv
        resultmv = f'<img src="{search_and_down(name)}">'
        mv_url = search_and_down(name)
        download_poster = down_req(name, mv_url)
        db.db.collection.insert_one({"mvname" : name, "mvurl" : mv_url, 'UploadDate' : datetime.now()})
        return render_template("result.html") + resultmv + '<a href="resultmv" download></a>'

    return render_template("result.html") + resultmv


@app.route("/list", methods=['GET', 'POST'])
def database_list():
    emp_list = db.db.collection.find()
    return render_template('list.html',emp_list=emp_list)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        delete_option = request.form.to_dict()
        delete_name = delete_option["fname"]
        delquery = {"mvname" : delete_name}
        db.db.collection.delete_one(delquery)
        poster_list = db.db.collection.find()
        return render_template('delete.html', poster_list=poster_list) + "<h1>Poster deleted</h1>"
    return render_template('delete.html')

@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


#return f'<img src="{search_and_down(name)}">'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

