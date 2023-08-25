"""Database model for Bleeze"""

import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store(db.Model):
    """A store"""

    __tablename__="stores"

    id = db.Column(db.Integer, autoincrement=True, primarykey=True)
    store_number = db.Column(db.Integer, unique = True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip = db.Column(db.Integer)

    unit = db.relationship("Unit", backref = "units")
    retail_items = db.relationship("Retail Items", backref = "retail items")

    def __repr__(self):
        return f'Store number: {self.store_number} -- {self.city}, {self.state}'


# UNITS
# many units per store
# multiple units per contace

# RENTERS
#One renter can have multiple units

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