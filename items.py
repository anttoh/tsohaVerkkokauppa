from db import db
import makers


def get_id(item_name, maker_id):
    sql = "SELECT item_id FROM items WHERE name=:name AND maker_id=:maker_id"
    result = db.session.execute(sql, {"name": item_name, "maker_id": maker_id})
    return result.fetchone()


def add(item_name, maker_id):
    sql = "INSERT INTO items (name,maker_id) VALUES (:name,:maker_id)"
    db.session.execute(sql, {"name": item_name, "maker_id": maker_id})
    db.session.commit()


def get_and_add_if_nonexistent(item_name, maker_name):
    maker_id = makers.get_and_add_if_nonexistent(maker_name)
    item_id = get_id(item_name, maker_id)
    if item_id == None:
        add(item_name, maker_id)
        item_id = get_id(item_name, maker_id)
    return item_id[0]
