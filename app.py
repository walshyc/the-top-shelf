import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt



app = Flask(__name__)
app.config.from_object("config")
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'




mongo = PyMongo(app)



@app.route("/")
def home():
     
    if 'username' in session:
        user = session['username']
        signed_in = "You are signed in as " + user
        return render_template('index.html', user = user, categories=mongo.db.categories.find(), cocktails=mongo.db.cocktails.find())

    user_msg = 'You are not logged in'

    return render_template('index.html', message=user_msg, categories=mongo.db.categories.find(), cocktails=mongo.db.cocktails.find())


@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/logout')
def logout():
    session.pop('username', None)

    return redirect(url_for('home'))

@app.route('/login', methods=['POST', 'GET'])
def login():

        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username'].lower()})

        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) ==  login_user['password']:
                session['username'] = request.form['username'].lower()
                return redirect(url_for('home'))
        else:
            error = 'Incorrect Username/Password combination'
            return render_template('user.html', error_msg_login=error)

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username'].lower()})

        if existing_user is None:
            hashpassword = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {'name': request.form['username'].lower(), 'password': hashpassword})
            session['username'] = request.form['username'].lower()
            return redirect(url_for('home'))
        else:
            error = 'This username already exists'
            return render_template('user.html', error_msg_register=error)

    return render_template('user.html')

    return redirect(url_for('home'))


@app.route('/categories')
def categories():
    return render_template('categories.html', categories=mongo.db.categories.find())


@app.route('/categories/<category_name>')
def category_name(category_name):
    the_category = mongo.db.categories.find_one({"category_name": category_name})
    return render_template("drink.html", categories=mongo.db.categories.find(), category=the_category, cocktails=mongo.db.cocktails.find())

@app.route('/<username>')
def user_drinks(username):
    if 'username' in session:
        user = session['username']
    user_drinks = mongo.db.categories.find()
    the_category = mongo.db.categories.find_one()
    return render_template("user_cocktails.html", categories=mongo.db.categories.find(), cocktails=mongo.db.cocktails.find(), category=the_category, user=user)

@app.route('/categories/<category_name>/<cocktail_name>')
def cocktail_id_long(category_name, cocktail_name):
     the_category = mongo.db.categories.find_one({"category_name": category_name})
     all_cocktails = mongo.db.cocktails.find()
     the_cocktail = mongo.db.cocktails.find_one({"cocktail_name": cocktail_name})
     return render_template("single.html", category = the_category, categories=mongo.db.categories.find(),  cocktails = mongo.db.cocktails.find(), cocktail = the_cocktail)


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
    
    cocktails.insert({'added_by': session['username'],
                      'cocktail_base': request.form['cocktail_base'],
                      'cocktail_name': request.form['cocktail_name'],
                      'image': request.form['cocktail_url'],
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


@app.route('/edit_cocktail/<cocktail_name>')
def edit_cocktail(cocktail_name):
    the_cocktail = mongo.db.cocktails.find_one({"cocktail_name": cocktail_name})
    return render_template('editcocktail.html',  drink = the_cocktail,  categories=mongo.db.categories.find())

@app.route('/update_cocktail/<cocktail_name>', methods=['POST'])
def update_cocktail(cocktail_name):
    cocktails = mongo.db.cocktails
    cocktails.update( {"cocktail_name": cocktail_name}, 
                 {    'added_by': session['username'], 
                      'cocktail_base': request.form['cocktail_base'],
                      'cocktail_name': request.form['cocktail_name'],
                      'image': request.form['cocktail_url'],
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
                            {
                                "step_text": request.form.get('method4')
                            },
                             ]
        })
    return redirect(url_for('categories'))


@app.route('/delete_cocktail/<cocktail_name>')
def delete_cocktail(cocktail_name):
    mongo.db.cocktails.remove({"cocktail_name": cocktail_name})
    return redirect(url_for('categories'))
    

if __name__ == "__main__":
    app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get('PORT')),
    debug=True)
