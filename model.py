"""Database model for Bleeze"""

import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store(db.Model):
    """A store"""

    __tablename__= "stores"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip = db.Column(db.Integer)

    units = db.relationship("Unit", backref = "store")
    retail_items = db.relationship("Retail", backref = "store")

    def __repr__(self):
        return f'Store number: {self.store_number} -- {self.city}, {self.state}'
    
class Renter(db.Model):
    """A renter."""

    __tablename__ = "renters"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    month_of_birth = db.Column(db.String(14))
    day_of_birth = db.Column(db.Integer)
    year_of_birth = db.Column(db.Integer)
    street_address = db.Column(db.String(75))
    city = db.Column(db.String(75))
    state = db.Column(db.String(15))
    zip = db.Column(db.Integer)
    phone_number = db.Column(db.String(15))
    email = db.Column(db.String(30))
    

    units = db.relationship("Unit", backref = "renter")

    def __repr__(self):
        return f'Renter: {self.first_name} {self.last_name}'
    
class Unit(db.Model):
    """A unit."""

    __tablename__= "units"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    unit_number = db.Column(db.String(255), unique = True)
    size = db.Column(db.String(50))
    rented = db.Column(db.Boolean, default = False)
    digital_access = db.Column(db.Boolean)
    type = db.Column(db.String(50))

    renter_id = db.Column(db.Integer, db.ForeignKey('renters.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)


    def __repr__(self):
        return f'Unit number: {self.unit_number}'


class Retail(db.Model):
    """A retail item."""

    __tablename__ = "retail_items"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_name = db.Column(db.String(50))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    def __repr__(self):
        return f'Retail item: {self.item_name}'


def connect_to_db(flask_app, db_uri=os.environ["POSTGRES_URI"], echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Database connected.")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)