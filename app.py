import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'theTopShelf'
app.config["MONGO_URI"] = 'mongodb+srv://root:jk6200dl@myfirstcluster-fdipx.mongodb.net/theTopShelf?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template('index.html', categories=mongo.db.categories.find(), cocktails = mongo.db.cocktails.find())

@app.route('/categories')
def categories():
    return render_template('categories.html', categories=mongo.db.categories.find())

@app.route('/categories/<category_id>')
def category_id(category_id):
    the_category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("drink.html",categories=mongo.db.categories.find(), category = the_category, cocktails = mongo.db.cocktails.find())

# @app.route('/categories/<category_id>/<cocktail_id>')
# def cocktail_id(category_id, cocktail_id):
#     the_category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
#     all_cocktails = mongo.db.cocktails.find()
#     the_cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
#     return render_template("single.html", category = the_category, categories=mongo.db.categories.find(),  cocktails = mongo.db.cocktails.find(), cocktail = the_cocktail)

@app.route('/<cocktail_id>')
def cocktail_id(cocktail_id):
    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    

    return render_template("single.html", cocktail = cocktail )

@app.route('/add_cocktail')
def add_cocktail():
    return render_template('addcocktail.html', categories=mongo.db.categories.find())

@app.route('/insert_cocktail', methods=['POST'])
def insert_cocktail():
    cocktails = mongo.db.cocktails
    cocktails.insert_one(request.form.to_dict()) 
    return redirect(url_for('categories'))


if __name__ == "__main__":
    app.run(host = os.environ.get("IP"),
    port=int(os.environ.get('PORT')),
    debug=True)