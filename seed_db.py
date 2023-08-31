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

db.create_all()


#STORE
store1 = Store(store_number = 2055, address = "450 South Nuggets Way", city = "Denver", state = "Colorado", zip = 80014)
store2 = Store(store_number=3001, address="123 Main Street", city="New York", state="New York", zip=10001)
store3 = Store(store_number=4567, address="789 Elm Avenue", city="Los Angeles", state="California", zip=90001)
store4 = Store(store_number=8012, address="456 Oak Road", city="Chicago", state="Illinois", zip=60601)
store5 = Store(store_number=6023, address="789 Maple Lane", city="San Francisco", state="California", zip=94101)
store6 = Store(store_number=9876, address="101 Pine Street", city="Seattle", state="Washington", zip=98101)
store7 = Store(store_number=2345, address="567 Cedar Drive", city="Miami", state="Florida", zip=33101)
store8 = Store(store_number=1111, address="222 Birch Street", city="Houston", state="Texas", zip=77001)
store9 = Store(store_number=4444, address="333 Redwood Lane", city="Atlanta", state="Georgia", zip=30301)
store10 = Store(store_number=7777, address="888 Sequoia Road", city="Boston", state="Massachusetts", zip=54435)
store11 = Store(store_number=1234, address="555 Willow Street", city="Phoenix", state="Arizona", zip=85001)
store12 = Store(store_number=9870, address="123 Elm Avenue", city="Dallas", state="Texas", zip=75201)
store13 = Store(store_number=5678, address="456 Oak Drive", city="San Diego", state="California", zip=92101)
store14 = Store(store_number=3333, address="777 Maple Lane", city="Portland", state="Oregon", zip=97201)
store15 = Store(store_number=8888, address="101 Pine Road", city="Minneapolis", state="Minnesota", zip=55401)
store16 = Store(store_number=5555, address="222 Cedar Street", city="Las Vegas", state="Nevada", zip=89101)
store17 = Store(store_number=2222, address="888 Birch Drive", city="Philadelphia", state="Pennsylvania", zip=19101)
store18 = Store(store_number=6666, address="333 Redwood Road", city="Detroit", state="Michigan", zip=48201)
store19 = Store(store_number=4444, address="999 Sequoia Avenue", city="Orlando", state="Florida", zip=32801)
store20 = Store(store_number=1111, address="777 Redwood Drive", city="San Antonio", state="Texas", zip=78201)
store21 = Store(store_number=6789, address="123 Salt Lake Avenue", city="Salt Lake City", state="Utah", zip=84101)

db.session.add_all([
    store1, store2, store3, store4, store5,
    store6, store7, store8, store9, store10,
    store11, store12, store13, store14, store15,
    store16, store17, store18, store19, store20,
    store21
])



db.session.commit()

#RENTER

#UNIT

#RETAIL

