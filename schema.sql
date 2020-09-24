CREATE TABLE users
(
    user_id SERIAL,
    username TEXT UNIQUE,
    password TEXT,
    PRIMARY KEY(user_id)
);

CREATE TABLE makers
(
    maker_id SERIAL,
    name TEXT UNIQUE,
    PRIMARY KEY(maker_id)
);

CREATE TABLE items
(
    item_id SERIAL,
    maker_id INT,
    name TEXT,
    visible INT,
    PRIMARY KEY(item_id),
    FOREIGN KEY(maker_id) REFERENCES makers(maker_id)
);

CREATE TABLE listings
(
    listing_id SERIAL,
    seller_id INT,
    item_id INT,
    price DECIMAL,
    tags TEXT,
    visible INT,
    PRIMARY KEY(listing_id),
    FOREIGN KEY(seller_id) REFERENCES users(user_id),
    FOREIGN KEY(item_id) REFERENCES items(item_id)
);

CREATE TABLE orders
(
    order_id SERIAL,
    buyer_id INT,
    listing_id INT,
    sent INT,
    PRIMARY KEY(order_id),
    FOREIGN KEY(buyer_id) REFERENCES users(user_id),
    FOREIGN KEY(listing_id) REFERENCES listings(listing_id)
);