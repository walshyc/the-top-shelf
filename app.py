import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt


app = Flask(__name__)
app.config.from_object("config")

mongo = PyMongo(app)


# Route for the homepage
@app.route("/")
def home():

    categories = mongo.db.categories.find()
    cocktails = mongo.db.cocktails.find()

    # Checks if the user is logged in
    if 'username' in session:
        user = session['username']
        return render_template('index.html', user=user, categories=categories, cocktails=cocktails)

    return render_template('index.html', categories=categories, cocktails=cocktails)

# Route to display the User login or register page
@app.route('/user')
def user():
    return render_template('user.html')


# Route to log a user out of their account
@app.route('/logout')
def logout():
    session.pop('username', None)

    return redirect(url_for('home'))


# Route to login a user
@app.route('/login', methods=['POST', 'GET'])
def login():

    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username'].lower()})


    if request.form['password'] == "" :
            error = "Password can't be empty"
            return render_template('user.html', error_msg_login=error)

    elif request.form['username'] == "" :
            error = "Username can't be empty"
            return render_template('user.html', error_msg_login=error)

    # Checks if the user is logged in
    elif login_user:
        # Checks if the password entered matches the password in the database
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username'].lower()
            return redirect(url_for('home'))
    else:
        # Shows an error if the correct credentials aren't given
        error = 'Incorrect Username/Password combination'
        return render_template('user.html', error_msg_login=error)

# Route to register a user
@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        users = mongo.db.users
        existing_user = users.find_one(
            {'name': request.form['username'].lower()})

        # Checks is the password field is empty
        if request.form['password'] == "" :
            error = "Password can't be empty"
            return render_template('user.html', error_msg_register=error)
        
        #Checks if the password field is empty
        elif request.form['username'] == "" :
            error = "Username can't be empty"
            return render_template('user.html', error_msg_register=error)

        # Checks if the username doesn't already exist
        elif existing_user is None:
            # Creates a hash of the password to ensure it is stored securly in the database
            hashpassword = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())

            # adds the new user to the users table in the database
            users.insert(
                {'name': request.form['username'].lower(), 'password': hashpassword})
            session['username'] = request.form['username'].lower()
            return redirect(url_for('home'))

        else:
            # Gives an error message if the username already exists in the database
            error = 'This username already exists'
            return render_template('user.html', error_msg_register=error)


    return render_template('user.html')


# Route to display the categories
@app.route('/categories')
def categories():
    categories = mongo.db.categories.find()
    return render_template('categories.html', categories=categories)


# Route to display all ther cocktails within a category
@app.route('/categories/<category_name>')
def category_name(category_name):
    the_category = mongo.db.categories.find_one(
        {"category_name": category_name})
    categories = mongo.db.categories.find()
    cocktails = mongo.db.cocktails.find()
    return render_template("drink.html", categories=categories, category=the_category, cocktails=cocktails)

# Diaplsy the logged in users list of cockatils and gives them options for editing or deleting
@app.route('/<username>')
def user_drinks(username):
    if 'username' in session:
        user = session['username']
    categories = mongo.db.categories.find()
    cocktails = mongo.db.cocktails.find()
    the_category = mongo.db.categories.find_one()

    return render_template("user_cocktails.html", categories=categories, cocktails=cocktails, category=the_category, user=user)

# Route to display a single cocktail page with all its data displayed
@app.route('/categories/<category_name>/<cocktail_name>')
def cocktail_id_long(category_name, cocktail_name):
    the_category = mongo.db.categories.find_one(
        {"category_name": category_name})
    all_cocktails = mongo.db.cocktails.find()
    the_cocktail = mongo.db.cocktails.find_one(
        {"cocktail_name": cocktail_name})
    categories = mongo.db.categories.find()

    return render_template("single.html", category=the_category, categories=categories,  cocktails=all_cocktails, cocktail=the_cocktail)

# Route to allow the user to add a new cockatil to the database
@app.route('/add_cocktail')
def add_cocktail():
    categories=mongo.db.categories.find()
    return render_template('addcocktail.html', categories=categories)


# Route that adds the form data to the database for a new cocktail
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
        {
            "step_text": request.form.get('method5')
        }
    ]
    })

    return redirect(url_for('categories'))


# Route that allows the user to edit an existing cocktail
@app.route('/edit_cocktail/<cocktail_name>')
def edit_cocktail(cocktail_name):
    the_cocktail = mongo.db.cocktails.find_one(
        {"cocktail_name": cocktail_name})
    return render_template('editcocktail.html',  drink=the_cocktail,  categories=mongo.db.categories.find())


# Route that sends the edited cocktail form data to the database and updates the record
@app.route('/update_cocktail/<cocktail_name>', methods=['POST'])
def update_cocktail(cocktail_name):
    cocktails = mongo.db.cocktails
    cocktails.update({"cocktail_name": cocktail_name},
                     {'added_by': session['username'],
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
            "step_text": request.form.get('method5')
        }
                     ]
    })
    return redirect(url_for('categories'))


# Route that allows the user to delete a cocktail from the database
@app.route('/delete_cocktail/<cocktail_name>')
def delete_cocktail(cocktail_name):
    mongo.db.cocktails.remove({"cocktail_name": cocktail_name})
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get('PORT')),
            debug=True)
