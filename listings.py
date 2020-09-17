from flask import session
from db import db
import items


def get(listing_id):
    sql = "SELECT * FROM listings"
    result = db.session.execute(sql)
    return result.fetchone()


def get_list(item_id):
    sql = "SELECT listings.price, users.username, listings.listing_id FROM listings INNER JOIN items ON listings.item_id=items.item_id INNER JOIN users ON listings.seller_id=users.user_id WHERE items.item_id=:item_id"
    result = db.session.execute(sql, {"item_id": item_id})
    return result.fetchall()


def create(item_name, maker_name, price, categories_list):
    try:
        item_id = items.get_and_add_if_nonexistent(item_name, maker_name)
        sql = "INSERT INTO listings (price,item_id,seller_id) VALUES (:price,:item_id,:seller_id)"
        db.session.execute(
            sql, {"price": price, "item_id": item_id, "seller_id": session["user_id"]})
        db.session.commit()
        return True
    except:
        return False
