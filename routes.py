from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app
import users
import listings
import items
import orders


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


@app.route("/profile")
def view_profile():
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("profile.html")


@app.route("/items")
def view_items():
    if users.username() == 0:
        return redirect("/")
    else:
        try:
            query_string = request.args["query"]
            query_list = query_string.split(",")
        except:
            query_list = [""]

        return render_template("items.html", list=items.get_list(query_list))


@app.route("/bought")
def view_bought_items():
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("bought.html", list=orders.bought_items())


@app.route("/sold")
def view_sold_items():
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("sold.html", list=orders.sold_items())


@app.route("/unsold")
def view_unsold_items():
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("sold.html", list=listings.unsold_items())


@app.route("/active_orders")
def view_active_orders():
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("active_orders.html", list=orders.active_orders())


@app.route("/orders")
def view_orders():
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("orders.html", list=orders.pending_orders())


@app.route("/listings/<item_id>")
def view_listings(item_id):
    if users.username() == 0:
        return redirect("/")
    else:
        return render_template("listings.html", item=items.get(item_id), list=listings.get_list(item_id))


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
        tags = request.form["categories"]
        if listings.create(item_name, maker_name, price, tags):
            return redirect("/home")
        else:
            return render_template("error.html", message="Failed to create a listing")


@app.route("/buy/<listing_id>", methods=["post"])
def view_listing(listing_id):
    if users.username() == 0:
        return redirect("/")
    if request.method == "POST":
        orders.create(listing_id)
        return redirect("/home")


@app.route("/send/<order_id>", methods=["post"])
def view_order(order_id):
    if users.username() == 0:
        return redirect("/")
    if request.method == "POST":
        orders.send(order_id)
        return redirect("/home")


@app.route("/cancel_order/<order_id>", methods=["post"])
def cancel_order(order_id):
    if users.username() == 0:
        return redirect("/")
    if request.method == "POST":
        orders.cancel(order_id)
        return redirect("/home")
