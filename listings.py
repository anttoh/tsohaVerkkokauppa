from flask import session
from db import db
import items


def get(listing_id):
    sql = "SELECT * FROM listings WHERE listing_id=:listing_id"
    result = db.session.execute(sql, {"listing_id": listing_id})
    return result.fetchone()


def hide(listing_id):
    sql = "UPDATE listings SET visible = 0 WHERE listing_id = :listing_id"
    db.session.execute(
        sql, {"listing_id": listing_id})
    db.session.commit()


def set_visible(listing_id):
    sql = "UPDATE listings SET visible = 1 WHERE listing_id = :listing_id"
    db.session.execute(
        sql, {"listing_id": listing_id})
    db.session.commit()


def get_list(item_id):
    sql = "SELECT listings.price, users.username, listings.listing_id, listings.tags FROM listings INNER JOIN items ON listings.item_id=items.item_id INNER JOIN users ON listings.seller_id=users.user_id WHERE items.item_id=:item_id AND listings.visible=1 AND listings.seller_id!=:user_id"
    result = db.session.execute(
        sql, {"item_id": item_id, "user_id": session["user_id"]})
    return result.fetchall()


def delete(listing_id):
    sql = "DELETE FROM listings WHERE listing_id=:listing_id"
    db.session.execute(sql, {"listing_id": listing_id})
    db.session.commit()


def unsold_items():
    sql = "SELECT listings.listing_id, items.name FROM listings INNER JOIN items ON listings.item_id=items.item_id WHERE listings.seller_id=:user_id AND listings.visible=1"
    result = db.session.execute(sql, {"user_id": session["user_id"]})
    return result.fetchall()


def create(item_name, maker_name, price, tags):
    item_id = items.get_and_add_if_nonexistent(item_name, maker_name)
    sql = "INSERT INTO listings (item_id,seller_id,price,tags,visible) VALUES (:item_id,:seller_id,:price,:tags,:visible)"
    db.session.execute(
        sql, {"item_id": item_id, "seller_id": session["user_id"], "price": price, "tags": tags, "visible": 1})
    db.session.commit()
