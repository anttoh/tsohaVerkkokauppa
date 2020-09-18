from db import db
import makers
import listings


def filter_items_without_listings(item):
    num_of_listings = len(listings.get_list(item[2]))
    return num_of_listings != 0


def get_list():
    sql = "SELECT items.name, makers.name, items.item_id FROM items INNER JOIN makers ON items.maker_id=makers.maker_id"
    result = db.session.execute(sql)
    items = result.fetchall()
    filtered_items = filter(filter_items_without_listings, items)
    return filtered_items


def get(item_id):
    sql = "SELECT items.name, makers.name, items.item_id FROM items INNER JOIN makers ON items.maker_id=makers.maker_id WHERE items.item_id=:item_id"
    result = db.session.execute(sql, {"item_id": item_id})
    return result.fetchone()


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
