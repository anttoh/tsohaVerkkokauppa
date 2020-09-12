from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app
import users
import listings


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/home")
        else:
            return render_template("error.html", message="Incorrect username or password")


@app.route("/logout")
def logout():
    if users.username() != 0:
        users.logout()

    return redirect("/")


@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Failed to register")


@app.route("/home")
def home():
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("home.html", username=users.username())


@app.route("/view_listings")
def view_listings():
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("view_listings.html", list=listings.get_list())


@app.route("/create_listing", methods=["get", "post"])
def create_listing():
    if users.username() == 0:
        return redirect("/")
    if request.method == "GET":
        return render_template("create_listing.html")
    if request.method == "POST":
        item_name = request.form["item"]
        maker_name = request.form["maker"]
        price = request.form["price"]
        categories_string = request.form["categories"]
        categories_list = categories_string.split(",")
        if listings.create(item_name, maker_name, price, categories_list):
            return redirect("/home")
        else:
            return render_template("error.html", message="Failed to create a listing")
