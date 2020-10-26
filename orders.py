from flask import session
from db import db
import listings


def get(order_id):
    sql = "SELECT * FROM orders WHERE order_id=:order_id"
    result = db.session.execute(sql, {"order_id": order_id})
    return result.fetchone()


def create(listing_id):
    sql = "INSERT INTO orders (buyer_id, listing_id, sent) VALUES (:buyer_id, :listing_id, :sent)"
    db.session.execute(
        sql, {"buyer_id": session["user_id"], "listing_id": listing_id, "sent": 0})
    db.session.commit()
    listings.hide(listing_id)


def cancel(order_id):
    sql = "DELETE FROM orders WHERE order_id=:order_id RETURNING listing_id"
    result = db.session.execute(sql, {"order_id": order_id})
    db.session.commit()
    listings.set_visible(result.fetchone()[0])


def send(order_id):
    sql = "UPDATE orders SET sent = 1 WHERE order_id = :order_id"
    db.session.execute(
        sql, {"order_id": order_id})
    db.session.commit()


def sold_items():
    sql = "SELECT items.name, makers.name, listings.price, users.username FROM orders INNER JOIN listings ON orders.listing_id=listings.listing_id INNER JOIN users ON orders.buyer_id=users.user_id INNER JOIN items ON listings.item_id=items.item_id INNER JOIN makers ON items.maker_id=makers.maker_id WHERE listings.seller_id=:user_id AND orders.sent=1"
    result = db.session.execute(sql, {"user_id": session["user_id"]})
    return result.fetchall()


def bought_items():
    sql = "SELECT items.name, makers.name, listings.price, users.username FROM orders INNER JOIN listings ON orders.listing_id=listings.listing_id INNER JOIN users ON listings.seller_id=users.user_id INNER JOIN items ON listings.item_id=items.item_id INNER JOIN makers ON items.maker_id=makers.maker_id WHERE orders.buyer_id=:user_id AND orders.sent=1"
    result = db.session.execute(sql, {"user_id": session["user_id"]})
    return result.fetchall()


def pending_orders():
    sql = "SELECT orders.order_id, items.name, makers.name, listings.price, users.username FROM orders INNER JOIN listings ON orders.listing_id=listings.listing_id INNER JOIN users ON orders.buyer_id=users.user_id INNER JOIN items ON listings.item_id=items.item_id INNER JOIN makers ON items.maker_id=makers.maker_id WHERE listings.seller_id=:user_id AND orders.sent=0"
    result = db.session.execute(sql, {"user_id": session["user_id"]})
    return result.fetchall()


def active_orders():
    sql = "SELECT orders.order_id, items.name, makers.name, listings.price, users.username FROM orders INNER JOIN listings ON orders.listing_id=listings.listing_id INNER JOIN users ON listings.seller_id=users.user_id INNER JOIN items ON listings.item_id=items.item_id INNER JOIN makers ON items.maker_id=makers.maker_id WHERE orders.buyer_id=:user_id AND orders.sent=0"
    result = db.session.execute(sql, {"user_id": session["user_id"]})
    return result.fetchall()
