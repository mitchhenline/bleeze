"""CRUD operations"""
from model import db, connect_to_db, Store, Renter, Unit, Retail


def get_units_by_store_id(store_id):
    return Unit.query.filter(Unit.store_id == store_id).all()

def is_valid_store(store_id):
    """Check if the store number exists in the database."""
    store = Store.query.filter_by(id=store_id).first()
    return store is not None