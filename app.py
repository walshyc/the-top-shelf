import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'theTopShelf'
app.config["MONGO_URI"] = 'mongodb+srv://root:jk6200dl@myfirstcluster-fdipx.mongodb.net/theTopShelf?retryWrites=true&w=majority'

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'


mongo = PyMongo(app)


@app.route("/")
def home():
    if 'username' in session:
        user_msg = 'You are logged in as ' + session['username']

    user_msg = 'You are not logged in'

    return render_template('index.html', message=user_msg, categories=mongo.db.categories.find(), cocktails=mongo.db.cocktails.find())


@app.route("/login")
def login():
    return ''


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpassword = bcrypt.hashpw(
                request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {'name': request.form['username'], 'password': hashpassword})
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            error = 'This username already exists'
            return render_template('register.html', error_msg=error)

    return render_template('register.html')

    return redirect(url_for('home'))


@app.route('/categories')
def categories():
    return render_template('categories.html', categories=mongo.db.categories.find())


@app.route('/categories/<category_id>')
def category_id(category_id):
    the_category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("drink.html", categories=mongo.db.categories.find(), category=the_category, cocktails=mongo.db.cocktails.find())

# @app.route('/categories/<category_id>/<cocktail_id>')
# def cocktail_id(category_id, cocktail_id):
#     the_category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
#     all_cocktails = mongo.db.cocktails.find()
#     the_cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
#     return render_template("single.html", category = the_category, categories=mongo.db.categories.find(),  cocktails = mongo.db.cocktails.find(), cocktail = the_cocktail)


@app.route('/<cocktail_id>')
def cocktail_id(cocktail_id):
    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    
    return render_template("single.html", cocktail=cocktail)


@app.route('/add_cocktail')
def add_cocktail():
    return render_template('addcocktail.html', categories=mongo.db.categories.find())


@app.route('/insert_cocktail', methods=['POST'])
def insert_cocktail():
    cocktails = mongo.db.cocktails

    cocktails.insert({'cocktail_base': request.form['cocktail_base'],
                      'cocktail_name': request.form['cocktail_name'],
                      'image': request.form['image'],
                      'short': request.form['short'],
                      "ingredients": [
                          {
                              "ing_name": request.form.get('ingredient_name0'),
                              "ing_amount": request.form.get('ingredient_amount0')
                          },
                          {
                              "ing_name": request.form.get('ingredient_name1'),
                              "ing_amount": request.form.get('ingredient_amount1')
                          },
                          {
                              "ing_name": request.form.get('ingredient_name2'),
                              "ing_amount": request.form.get('ingredient_amount2')
                          },
                          {
                              "ing_name": request.form.get('ingredient_name3'),
                              "ing_amount": request.form.get('ingredient_amount3')
                          },
                          {
                              "ing_name": request.form.get('ingredient_name4'),
                              "ing_amount": request.form.get('ingredient_amount4')
                          },
                          {
                              "ing_name": request.form.get('ingredient_name5'),
                              "ing_amount": request.form.get('ingredient_amount5')
                          }
                          
                      ],
                      "method": [{
                                "step_text": request.form.get('method0')
                            },
                            {
                                "step_text": request.form.get('method1')
                            },
                            {
                                "step_text": request.form.get('method2')
                            },
                            {
                                "step_text": request.form.get('method3')
                            },
                            {
                                "step_text": request.form.get('method4')
                            },
                             ]
                      })

    # cocktails.insert_one(request.form.to_dict())
    return redirect(url_for('categories'))


if __name__ == "__main__":
    app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get('PORT')),
    debug=True)
