from flask import session
from db import db
import listings


def get(order_id):
    sql = "SELECT * FROM orders WHERE order_id=:order_id"
    result = db.session.execute(sql, {"order_id": order_id})
    return result.fetchone()


def create(listing_id):
    try:
        sql = "INSERT INTO orders (buyer_id, listing_id, sent) VALUES (:buyer_id, :listing_id, :sent)"
        db.session.execute(
            sql, {"buyer_id": session["user_id"], "listing_id": listing_id, "sent": 0})
        db.session.commit()
        listings.hide(listing_id)
        return True
    except:
        return False


def send(order_id):
    sql = "UPDATE orders SET sent = 1 WHERE order_id = :order_id"
    db.session.execute(
        sql, {"order_id": order_id})
    db.session.commit()


def order_hisroty():
    sql = "SELECT orders.sent, items.name FROM orders INNER JOIN listings ON orders.listing_id=listings.listing_id INNER JOIN items ON listings.item_id=items.item_id WHERE orders.buyer_id=:user_id"
    result = db.session.execute(sql, {"user_id": session["user_id"]})
    return result.fetchall()


def active_orders():
    sql = "SELECT items.name, orders.order_id FROM orders INNER JOIN listings ON orders.listing_id=listings.listing_id INNER JOIN items ON listings.item_id=items.item_id WHERE listings.seller_id=:user_id AND orders.sent=0"
    result = db.session.execute(sql, {"user_id": session["user_id"]})
    return result.fetchall()
