from flask import session
from db import db


def create(listing_id):
    try:
        sql = "INSERT INTO orders (buyer_id, listing_id, sent) VALUES (:buyer_id, :listing_id, :sent)"
        db.session.execute(
            sql, {"buyer_id": session["user_id"], "listing_id": listing_id, "sent": 0})
        db.session.commit()
        return True
    except:
        return False


def send(order_id):
    sql = "UPDATE orders SET sent = 1 WHERE order_id = :order_id"
    db.session.execute(
        sql, {"order_id": order_id})
    db.session.commit()
