import os
from flask import (
     Flask, flash, render_template,
     request, redirect, url_for, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# main page route
@app.route("/")
@app.route("/all_recipes")
def all_recipes():
    receipes = list(mongo.db.receipes.find())
    return render_template("recipes.html", receipes=receipes)


# search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    receipes = list(mongo.db.receipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", receipes=receipes)


# register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if pass is confirmed 
        if request.form.get('password') == request.form.get('passwordConfirm'):
            # check if username already in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists")
                return redirect(url_for("register"))

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            # Put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successfull")
            return redirect(url_for("all_recipes"))
        else:
            flash("Passwords don't match!")
            return redirect(url_for('register'))

    return render_template("register.html")


# log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if user already in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # verify hashed pass match input
            if check_password_hash(
             existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(
                        url_for("all_recipes"))
            else:
                # invalid pass
                flash("Incorrect user and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect user and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


# logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("all_recipes"))


# add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        receipe = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients"),
            "portions": request.form.get("portions"),
            "how_to": request.form.get("how_to"),
            "author": session["user"]
        }
        mongo.db.receipes.insert_one(receipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("all_recipes"))

    return render_template("add_recipe.html")


# edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        receipe = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients"),
            "portions": request.form.get("portions"),
            "how_to": request.form.get("how_to"),
            "author": session["user"]
        }
        mongo.db.receipes.update({"_id": ObjectId(recipe_id)}, receipe)
        flash("Recipe Successfully Modified")
        return redirect(url_for("all_recipes"))

    recipe = mongo.db.receipes.find_one({"_id": ObjectId(recipe_id)})
    receipes = mongo.db.receipes.find().sort("name", 1)

    return render_template(
        "edit_recipe.html", recipe=recipe, receipes=receipes)


# delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.receipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("all_recipes"))


# admin - manage recipe
@app.route("/cookbook")
def cookbook():
    receipes = list(mongo.db.receipes.find().sort("name", 1))
    return render_template("cookbook.html", receipes=receipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
