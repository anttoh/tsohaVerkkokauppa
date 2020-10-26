from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app
import re
import users
import listings
import items
import orders
import makers
import tags


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
            return redirect("/opening")
        else:
            return render_template("error.html", message="Incorrect username or password")


@app.route("/logout")
def logout():
    if users.not_logged_in() == False:
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
            return render_template("error.html", message="Failed to register. Try choosing another username and make sure neither username or password are over 100 charecters long.")


@app.route("/opening")
def opening():
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("opening.html")


@app.route("/buyer")
def buyer():
    if users.not_logged_in():
        return redirect("/")
    else:
        session["role"] = "buyer"
        return render_template("buyer.html")


@app.route("/seller")
def seller():
    if users.not_logged_in():
        return redirect("/")
    else:
        session["role"] = "seller"
        return render_template("seller.html")


@ app.route("/profile")
def view_profile():
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("profile.html")


@ app.route("/items")
def view_items():
    if users.not_logged_in():
        return redirect("/")
    else:
        try:
            query_string = request.args["query"]
            query_list = query_string.split(",")
        except:
            query_list = [""]

        return render_template("items.html", list=items.get_list(query_list))


@ app.route("/bought")
def view_bought_items():
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("bought.html", list=orders.bought_items())


@ app.route("/sold")
def view_sold_items():
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("sold.html", list=orders.sold_items())


@ app.route("/unsold")
def view_unsold_items():
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("unsold.html", list=listings.unsold_items())


@ app.route("/active_orders")
def view_active_orders():
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("active_orders.html", list=orders.active_orders())


@ app.route("/orders")
def view_orders():
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("orders.html", list=orders.pending_orders())


@ app.route("/listings/<item_id>")
def view_listings(item_id):
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("listings.html", item=items.get(item_id), list=listings.get_list(item_id))


@ app.route("/maker/<maker_name>")
def view_maker(maker_name):
    if users.not_logged_in():
        return redirect("/")
    else:
        return render_template("maker.html", list=makers.get_list(maker_name))


@ app.route("/create_listing", methods=["get", "post"])
def create_listing():
    if users.not_logged_in():
        return redirect("/")
    if request.method == "GET":
        return render_template("create_listing.html")
    if request.method == "POST":
        item_name = request.form["item"]
        maker_name = request.form["maker"]
        price = request.form["price"]
        description = request.form["description"]
        tags = request.form["tags"]
        tags = re.split(" , |, | ,|,", tags)
        if listings.create(item_name, maker_name, price, description, tags):
            return redirect("/unsold")
        else:
            return render_template("error.html", message="Failed to create a listing. If you didn't leave the name of the item empty then you must have added too many tags or used too many charecters.")


@ app.route("/delete/<listing_id>", methods=["post"])
def remove_listing(listing_id):
    if users.not_logged_in():
        return redirect("/")
    if request.method == "POST":
        listings.delete(listing_id)
        return redirect("/unsold")


@ app.route("/buy/<listing_id>", methods=["post"])
def view_listing(listing_id):
    if users.not_logged_in():
        return redirect("/")
    if request.method == "POST":
        orders.create(listing_id)
        return redirect("/active_orders")


@ app.route("/send/<order_id>", methods=["post"])
def view_order(order_id):
    if users.not_logged_in():
        return redirect("/")
    if request.method == "POST":
        orders.send(order_id)
        return redirect("/sold")


@ app.route("/cancel_order/<order_id>", methods=["post"])
def cancel_order(order_id):
    if users.not_logged_in():
        return redirect("/")
    if request.method == "POST":
        orders.cancel(order_id)
        return redirect("/active_orders")


@ app.route("/reject_order/<order_id>", methods=["post"])
def reject_order(order_id):
    if users.not_logged_in():
        return redirect("/")
    if request.method == "POST":
        orders.cancel(order_id)
        return redirect("/orders")
