from db import db


def get_id(name):
    sql = """SELECT maker_id 
             FROM makers 
             WHERE name=:name"""
    result = db.session.execute(sql, {"name": name})
    return result.fetchone()


def add(name):
    sql = """INSERT INTO makers (name) 
             VALUES (:name)"""
    db.session.execute(sql, {"name": name})
    db.session.commit()


def get_and_add_if_nonexistent(name):
    maker_id = get_id(name)
    if maker_id == None:
        add(name)
        maker_id = get_id(name)
    return maker_id[0]


def get_list(name):
    sql = """SELECT name, item_id 
             FROM items 
             WHERE maker_id=:maker_id"""
    result = db.session.execute(sql, {"maker_id": get_id(name)[0]})
    return result.fetchall()
