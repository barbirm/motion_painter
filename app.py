import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/recommend")
def recommend():
    return render_template("recommendations.html")


@app.route("/get_reviews")
def get_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks if username exists inside db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists...")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Putting new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Making sure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_bucketlists"))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Takes the session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("profile"))


@app.route("/logout")
def logout():
    # Removes the user from session cookie
    flash("You have logged out successfully")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "genre_name": request.form.get("genre_name"),
            "movie_name": request.form.get("movie_name"),
            "movie_description": request.form.get("movie_description"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Added Successfully")
        return redirect(url_for("get_reviews"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_review.html", genres=genres)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name"),
            "movie_name": request.form.get("movie_name"),
            "movie_description": request.form.get("movie_description"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Updated Successfully")
        return redirect(url_for("get_reviews"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_review.html", review=review,  genres=genres)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("get_reviews"))


@app.route("/get_bucketlists")
def get_bucketlists():
    bucketlists = list(mongo.db.bucketlists.find().sort("bucketlist_name", 1))
    return render_template("bucketlists.html", bucketlists=bucketlists)


@app.route("/add_bucketlist", methods=["GET", "POST"])
def add_bucketlist():
    if request.method == "POST":
        bucketlist = {
            "bucketlist_name": request.form.get("bucketlist_name")
        }
        mongo.db.bucketlists.insert_one(bucketlist)
        flash("New Movie Added To Bucket List")
        return redirect(url_for("get_bucketlists"))

    return render_template("add_bucketlist.html")


@app.route("/edit_bucketlist/<bucketlist_id>", methods=["GET", "POST"])
def edit_bucketlist(bucketlist_id):
    if request.method == "POST":
        submit = {
            "bucketlist_name": request.form.get("bucketlist_name")
        }
        mongo.db.bucketlists.update({"_id": ObjectId(bucketlist_id)}, submit)
        flash("List Item Successfully Updated")
        return redirect(url_for("get_bucketlists"))

    bucketlist = mongo.db.bucketlists.find_one(
        {"_id": ObjectId(bucketlist_id)})
    return render_template("edit_bucketlist.html", bucketlist=bucketlist)


@app.route("/delete_bucketlist/<bucketlist_id>")
def delete_bucketlist(bucketlist_id):
    mongo.db.bucketlists.remove({"_id": ObjectId(bucketlist_id)})
    flash("List Item Successfully Deleted")
    return redirect(url_for("get_bucketlists"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
