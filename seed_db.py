import os
from flask import Flask

from model import db, connect_to_db, Store, Renter, Unit, Retail

app = Flask(__name__)

connect_to_db(app)

try:
    os.system("dropdb -U postgres bleeze")
    os.system("createdb -U postgres bleeze")

except:
    os.system("createdb bleeze")

db.create_all

