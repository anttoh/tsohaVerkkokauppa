from db import db


def get_id(name):
    sql = """SELECT tag_id 
             FROM tags 
             WHERE name=:name"""
    result = db.session.execute(sql, {"name": name})
    return result.fetchone()


def add(name):
    sql = """INSERT INTO tags (name) 
             VALUES (:name)"""
    db.session.execute(sql, {"name": name})
    db.session.commit()


def get_and_add_if_nonexistent(name):
    tag_id = get_id(name)
    if tag_id == None:
        add(name)
        tag_id = get_id(name)
    return tag_id[0]


def create_listing_tag(listing_id, tag_id):
    sql = """INSERT INTO listing_tag (listing_id, tag_id) 
             VALUES (:listing_id, :tag_id)"""
    db.session.execute(sql, {"listing_id": listing_id, "tag_id": tag_id})
    db.session.commit()


def get_list(listing_id):
    sql = """SELECT tags.name 
             FROM tags 
             INNER JOIN listing_tag ON tags.tag_id=listing_tag.tag_id 
             WHERE listing_tag.listing_id=:listing_id"""
    result = db.session.execute(sql, {"listing_id": listing_id})
    return result.fetchall()
