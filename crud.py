"""CRUD operations"""
from model import db, connect_to_db, Store, Renter, Unit, Retail


def get_units_by_store_id(store_id):
    return Unit.query.filter(Unit.store_id == store_id).all()

def get_store_by_id(store_id):
    return Store.query.filter(Store.id == store_id).first()

def get_retail_by_store_id(store_id):
    return Retail.query.filter(Retail.store_id == store_id).all()

def get_unit_by_id(unit_id):
    return Unit.query.filter(Unit.id == unit_id).first()

def is_valid_store(store_id):
    """Check if the store number exists in the database."""
    store = Store.query.filter_by(id=store_id).first()
    return store is not None