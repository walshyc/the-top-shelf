import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'theTopShelf'
app.config["MONGO_URI"] = 'mongodb+srv://root:jk6200dl@myfirstcluster-fdipx.mongodb.net/theTopShelf?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
@app.route('/categories')
def categories():
    return render_template('categories.html', categories=mongo.db.categories.find())



if __name__ == "__main__":
    app.run(host = os.environ.get("IP"),
    port=int(os.environ.get('PORT')),
    debug=True)