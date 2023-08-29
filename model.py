"""Database model for Bleeze"""

import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store(db.Model):
    """A store"""

    __tablename__= "stores"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    store_number = db.Column(db.Integer, unique = True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip = db.Column(db.Integer)

    units = db.relationship("Unit", backref = "store")
    retail_items = db.relationship("Retail_Items", backref = "store")

    def __repr__(self):
        return f'Store number: {self.store_number} -- {self.city}, {self.state}'
    
class Renter(db.Model):
    """A renter."""

    __tablename__ = "renters"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    # ADD MORE HERE

    units = db.relationship("Unit", backref = "renter")

    def __repr__(self):
        return f'Renter: {self.first_name} {self.last_name}'
    
class Unit(db.Model):
    """A unit."""

    __tablename__= "units"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    unit_number = db.Column(db.String(255), unique = True)
    size = db.Column(db.String(50))
    rented = db.Column(db.Boolean)
    digital_access = db.Column(db.Boolean)
    type = db.Column(db.String(50))

    renter_id = db.Column(db.Integer, db.ForeignKey('renters.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)


    def __repr__(self):
        return f'Unit number: {self.unit_number}'


# RETAIL ITEMS
# multiple retail items per store

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