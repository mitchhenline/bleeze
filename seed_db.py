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
store1 = Store(address="450 South Nuggets Way", city="Denver", state="Colorado", zip=80014)
store2 = Store(address="2525 E 3500 South", city="Salt Lake City", state="Utah", zip=84106)
store3 = Store(address="789 Elm Avenue", city="Los Angeles", state="California", zip=90001)
store4 = Store(address="456 Oak Road", city="Chicago", state="Illinois", zip=60601)
store5 = Store(address="789 Maple Lane", city="San Francisco", state="California", zip=94101)
store6 = Store(address="101 Pine Street", city="Seattle", state="Washington", zip=98101)
store7 = Store(address="567 Cedar Drive", city="Miami", state="Florida", zip=33101)
store8 = Store(address="222 Birch Street", city="Houston", state="Texas", zip=77001)
store9 = Store(address="333 Redwood Lane", city="Atlanta", state="Georgia", zip=30301)
store10 = Store(address="888 Sequoia Road", city="Boston", state="Massachusetts", zip=54435)
store11 = Store(address="555 Willow Street", city="Phoenix", state="Arizona", zip=85001)
store12 = Store(address="123 Elm Avenue", city="Dallas", state="Texas", zip=75201)
store13 = Store(address="456 Oak Drive", city="San Diego", state="California", zip=92101)
store14 = Store(address="777 Maple Lane", city="Portland", state="Oregon", zip=97201)
store15 = Store(address="101 Pine Road", city="Minneapolis", state="Minnesota", zip=55401)
store16 = Store(address="222 Cedar Street", city="Las Vegas", state="Nevada", zip=89101)
store17 = Store(address="888 Birch Drive", city="Philadelphia", state="Pennsylvania", zip=19101)
store18 = Store(address="333 Redwood Road", city="Detroit", state="Michigan", zip=48201)
store19 = Store(address="999 Sequoia Avenue", city="Orlando", state="Florida", zip=32801)
store20 = Store(address="777 Redwood Drive", city="San Antonio", state="Texas", zip=78201)
store21 = Store(address="123 Salt Lake Avenue", city="Salt Lake City", state="Utah", zip=84101)


db.session.add_all([
    store1, store2, store3, store4, store5,
    store6, store7, store8, store9, store10,
    store11, store12, store13, store14, store15,
    store16, store17, store18, store19, store20,
    store21
])


#RENTER

renter1 = Renter(first_name = "Mitch", last_name = "Henline", month_of_birth = "August", day_of_birth = 31, year_of_birth = 1974, street_address = "556 Water Street", city = "Tallahasee", state = "Florida", zip = "51323", phone_number = "762-554-0953")
renter2 = Renter(first_name="Catherine", last_name="Major", month_of_birth="April", day_of_birth=12, year_of_birth=1988, street_address="123 Giggles Avenue", city="Los Angeles", state="California", zip="98765", phone_number="555-123-4567")
renter3 = Renter(first_name="Cesar", last_name="Perez", month_of_birth="February", day_of_birth=29, year_of_birth=1992, street_address="789 Chuckle Road", city="New York", state="New York", zip="12345", phone_number="555-987-6543")
renter4 = Renter(first_name="Nathan", last_name="Searle", month_of_birth="July", day_of_birth=7, year_of_birth=1977, street_address="456 Laughter Lane", city="Miami", state="Florida", zip="54321", phone_number="555-789-1234")
renter5 = Renter(first_name="Jon", last_name="Luker", month_of_birth="December", day_of_birth=25, year_of_birth=1985, street_address="321 Chuckle Street", city="Chicago", state="Illinois", zip="13579", phone_number="555-456-7890")
renter6 = Renter(first_name="Blake", last_name="White", month_of_birth="May", day_of_birth=16, year_of_birth=1990, street_address="567 Guffaw Avenue", city="Houston", state="Texas", zip="56789", phone_number="555-234-5678")
renter7 = Renter(first_name="Paul", last_name="Nisonger", month_of_birth="September", day_of_birth=3, year_of_birth=1983, street_address="234 Giggles Lane", city="San Francisco", state="California", zip="98765", phone_number="565-876-5432")
renter8 = Renter(first_name="Alex", last_name="Sylveseter", month_of_birth="March", day_of_birth=8, year_of_birth=1978, street_address="890 Chuckle Road", city="Denver", state="Colorado", zip="54321", phone_number="555-765-4321")
renter9 = Renter(first_name="Chad", last_name="Atkinson", month_of_birth="June", day_of_birth=19, year_of_birth=1995, street_address="432 Laugh Lane", city="Seattle", state="Washington", zip="24680", phone_number="555-654-3210")
renter10 = Renter(first_name="Tyler", last_name="Gerrard", month_of_birth="October", day_of_birth=10, year_of_birth=1980, street_address="111 Guffaw Street", city="Phoenix", state="Arizona", zip="13579", phone_number="555-321-6543")
renter11 = Renter(first_name="Mike", last_name="Palmer", month_of_birth="April", day_of_birth=1, year_of_birth=1989, street_address="222 Chuckle Avenue", city="Philadelphia", state="Pennsylvania", zip="98765", phone_number="555-987-1234")
renter12 = Renter(first_name="Austin", last_name="Taylor", month_of_birth="January", day_of_birth=5, year_of_birth=1991, street_address="333 Giggles Street", city="Atlanta", state="Georgia", zip="54321", phone_number="555-456-7890")
renter13 = Renter(first_name="Stanley", last_name="Rimer", month_of_birth="August", day_of_birth=20, year_of_birth=1987, street_address="444 Guffaw Lane", city="Dallas", state="Texas", zip="13579", phone_number="555-123-6543")
renter14 = Renter(first_name="Devvin", last_name="Kraatz", month_of_birth="November", day_of_birth=11, year_of_birth=1982, street_address="555 Chuckle Street", city="Miami", state="Florida", zip="24680", phone_number="555-789-0123")

db.session.add_all([
    renter1, renter2, renter3, renter4, renter5, renter6, renter7, renter8, renter9, renter10, renter11, renter12, renter13, renter14
])


#UNIT

unit1 = Unit(unit_number="A101", size="8x10", rented=True, digital_access=True, type="Climate Controlled", renter_id=1, store_id=2)
unit2 = Unit(unit_number="A102", size="8x10", rented=True, digital_access=False, type="Climate Controlled", renter_id=1, store_id=2)
unit3 = Unit(unit_number="A103", size="10x12", rented=True, digital_access=True, type="Climate Controlled", renter_id=3, store_id=2)
unit4 = Unit(unit_number="A104", size="10x12", rented=False, digital_access=False, type="Climate Controlled", renter_id=None, store_id=2)
unit5 = Unit(unit_number="A105", size="10x12", rented=True, digital_access=True, type="Climate Controlled", renter_id=5, store_id=2)
unit6 = Unit(unit_number="A106", size="10x12", rented=False, digital_access=False, type="Climate Controlled", renter_id=None, store_id=2)
unit7 = Unit(unit_number="A107", size="16x20", rented=True, digital_access=True, type="Climate Controlled", renter_id=7, store_id=2)
unit8 = Unit(unit_number="A108", size="16x20", rented=False, digital_access=False, type="Climate Controlled", renter_id=None, store_id=2)
unit9 = Unit(unit_number="A109", size="16x20", rented=True, digital_access=True, type="Climate Controlled", renter_id=9, store_id=2)
unit10 = Unit(unit_number="A110", size="16x20", rented=True, digital_access=False, type="Climate Controlled", renter_id=8, store_id=2)
unit11 = Unit(unit_number="B101", size="8x10", rented=True, digital_access=True, type="Climate Controlled", renter_id=11, store_id=2)
unit12 = Unit(unit_number="B102", size="8x10", rented=False, digital_access=False, type="Climate Controlled", renter_id=None, store_id=2)
unit13 = Unit(unit_number="B103", size="10x12", rented=True, digital_access=True, type="Climate Controlled", renter_id=13, store_id=2)
unit14 = Unit(unit_number="B104", size="10x12", rented=False, digital_access=False, type="Climate Controlled", renter_id=None, store_id=2)
unit15 = Unit(unit_number="B105", size="10x12", rented=True, digital_access=True, type="Climate Controlled", renter_id=1, store_id=2)
unit16 = Unit(unit_number="B106", size="10x12", rented=True, digital_access=False, type="Climate Controlled", renter_id=4, store_id=2)
unit17 = Unit(unit_number="B107", size="16x20", rented=True, digital_access=True, type="Climate Controlled", renter_id=3, store_id=2)
unit18 = Unit(unit_number="B108", size="16x20", rented=True, digital_access=False, type="Climate Controlled", renter_id=3, store_id=2)
unit19 = Unit(unit_number="B109", size="16x20", rented=True, digital_access=True, type="Climate Controlled", renter_id=5, store_id=2)
unit20 = Unit(unit_number="B110", size="16x20", rented=False, digital_access=False, type="Climate Controlled", renter_id=None, store_id=2)
unit21 = Unit(unit_number="P1", size="Parking", rented=True, digital_access=True, type="Parking", renter_id=7, store_id=2)
unit22 = Unit(unit_number="P2", size="Parking", rented=False, digital_access=False, type="Parking", renter_id=None, store_id=2)
unit23 = Unit(unit_number="P3", size="Parking", rented=True, digital_access=True, type="Parking", renter_id=9, store_id=2)
unit24 = Unit(unit_number="P4", size="Parking", rented=False, digital_access=False, type="Parking", renter_id=None, store_id=2)
unit25 = Unit(unit_number="P5", size="Parking", rented=True, digital_access=True, type="Parking", renter_id=11, store_id=2)
unit26 = Unit(unit_number="C01", size="10x12", rented=False, digital_access=False, type="Standard", renter_id=None, store_id=2)
unit27 = Unit(unit_number="C02", size="10x12", rented=True, digital_access=True, type="Standard", renter_id=13, store_id=2)
unit28 = Unit(unit_number="C03", size="10x12", rented=False, digital_access=False, type="Standard", renter_id=None, store_id=2)
unit29 = Unit(unit_number="C04", size="10x12", rented=True, digital_access=True, type="Standard", renter_id=1, store_id=2)
unit30 = Unit(unit_number="C05", size="10x12", rented=False, digital_access=False, type="Standard", renter_id=None, store_id=2)
unit31 = Unit(unit_number="C06", size="10x12", rented=False, digital_access=False, type="Standard", renter_id=None, store_id=2)


db.session.add_all([unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8, unit9, unit10, 
                   unit11, unit12, unit13, unit14, unit15, unit16, unit17, unit18, unit19, 
                   unit20, unit21, unit22, unit23, unit24, unit25, unit26, unit27, unit28, unit29, unit30, unit31])


#RETAIL

retail1 = Retail(item_name="Lock", price=10.99, quantity=50, store_id=2)
retail4 = Retail(item_name="Combination Lock", price=15.99, quantity=30, store_id=2)
retail2 = Retail(item_name="Small Box", price=3.99, quantity=100, store_id=2)
retail6 = Retail(item_name="Medium Box", price=4.99, quantity=80, store_id=2)
retail10 = Retail(item_name="Big Box", price=5.99, quantity=90, store_id=2)
retail3 = Retail(item_name="Packing Peanuts", price=4.99, quantity=10, store_id=2)
retail5 = Retail(item_name="Shrink Wrap", price=10.99, quantity=4, store_id=2)
retail7 = Retail(item_name="Small Roll Tape", price=4.29, quantity=15, store_id=2)
retail8 = Retail(item_name="Large Roll Tape", price=5.99, quantity=25, store_id=2)
retail9 = Retail(item_name="Masking Tape", price=3.99, quantity=45, store_id=2)
retail11 = Retail(item_name="Cleaning Wipes", price=4.99, quantity=18, store_id=2)
retail12 = Retail(item_name="Tarp", price=17.29, quantity=5, store_id=2)

retail13 = Retail(item_name="Lock", price=10.99, quantity=55, store_id=4)
retail14 = Retail(item_name="Box", price=5.99, quantity=75, store_id=4)
retail15 = Retail(item_name="Tape", price=1.99, quantity=170, store_id=4)
retail16 = Retail(item_name="Combination Lock", price=15.99, quantity=28, store_id=4)

retail17 = Retail(item_name="Lock", price=10.99, quantity=48, store_id=5)
retail18 = Retail(item_name="Box", price=5.99, quantity=88, store_id=5)
retail19 = Retail(item_name="Tape", price=1.99, quantity=160, store_id=5)
retail20 = Retail(item_name="Combination Lock", price=15.99, quantity=33, store_id=5)

retail21 = Retail(item_name="Lock", price=10.99, quantity=53, store_id=6)
retail22 = Retail(item_name="Box", price=5.99, quantity=95, store_id=6)
retail23 = Retail(item_name="Tape", price=1.99, quantity=175, store_id=6)
retail24 = Retail(item_name="Combination Lock", price=15.99, quantity=27, store_id=6)

retail25 = Retail(item_name="Lock", price=10.99, quantity=60, store_id=7)
retail26 = Retail(item_name="Box", price=5.99, quantity=85, store_id=7)
retail27 = Retail(item_name="Tape", price=1.99, quantity=190, store_id=7)
retail28 = Retail(item_name="Combination Lock", price=15.99, quantity=40, store_id=7)

retail29 = Retail(item_name="Lock", price=10.99, quantity=38, store_id=8)
retail30 = Retail(item_name="Box", price=5.99, quantity=70, store_id=8)
retail31 = Retail(item_name="Tape", price=1.99, quantity=155, store_id=8)
retail32 = Retail(item_name="Combination Lock", price=15.99, quantity=23, store_id=8)

db.session.add_all([retail1, retail2, retail3, retail4, retail5, retail6, retail7, retail8,
                   retail9, retail10, retail11, retail12, retail13, retail14, retail15, retail16,
                   retail17, retail18, retail19, retail20, retail21, retail22, retail23, retail24,
                   retail25, retail26, retail27, retail28, retail29, retail30, retail31, retail32])

db.session.commit()
