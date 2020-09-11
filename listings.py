from flask import session
from db import db
import items


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
