from db import db
import makers
import listings


def get_list(searchwords):
    sql = "SELECT items.name, makers.name, items.item_id FROM items INNER JOIN makers ON items.maker_id=makers.maker_id"
    result = db.session.execute(sql)
    items = result.fetchall()
    filtered_items = []
    found = False
    for item in items:
        items_listings = listings.get_list(item[2])
        if len(items_listings) == 0:
            continue
        for word in searchwords:
            if word in item[0] or word in item[1]:
                filtered_items.insert(0, item)
                break
            else:
                for listing in items_listings:
                    if word in listing[3]:
                        filtered_items.append(item)
                        found = True
                        break
                if found:
                    found = False
                    break
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
