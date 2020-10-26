from flask import session
from db import db
import items
import tags


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
    sql = "SELECT listings.price, users.username, listings.description, listings.listing_id FROM listings INNER JOIN items ON listings.item_id=items.item_id INNER JOIN users ON listings.seller_id=users.user_id WHERE items.item_id=:item_id AND listings.visible=1 AND listings.seller_id!=:user_id"
    result = db.session.execute(
        sql, {"item_id": item_id, "user_id": session["user_id"]})
    return result.fetchall()


def delete(listing_id):
    sql = "DELETE FROM listing_tag WHERE listing_id=:listing_id"
    db.session.execute(sql, {"listing_id": listing_id})
    db.session.commit()
    sql = "DELETE FROM listings WHERE listing_id=:listing_id"
    db.session.execute(sql, {"listing_id": listing_id})
    db.session.commit()


def unsold_items():
    sql = "SELECT listings.listing_id, items.name, makers.name, listings.price FROM listings INNER JOIN items ON listings.item_id=items.item_id INNER JOIN makers ON items.maker_id=makers.maker_id WHERE listings.seller_id=:user_id AND listings.visible=1"
    result = db.session.execute(sql, {"user_id": session["user_id"]})
    return result.fetchall()


def create(item_name, maker_name, price, description, tags_list):
    if len(tags_list) > 100 or len(item_name) < 1:
        return False
    try:
        item_id = items.get_and_add_if_nonexistent(item_name, maker_name)
        sql = "INSERT INTO listings (item_id,seller_id,price,description,visible) VALUES (:item_id,:seller_id,:price,:description,:visible) RETURNING listing_id"
        result = db.session.execute(
            sql, {"item_id": item_id, "seller_id": session["user_id"], "price": price, "description": description, "visible": 1})
        db.session.commit()
        listing_id = result.fetchone()[0]
        for tag in tags_list:
            tag_id = tags.get_and_add_if_nonexistent(tag)
            tags.create_listing_tag(listing_id, tag_id)
        return True
    except:
        return False
