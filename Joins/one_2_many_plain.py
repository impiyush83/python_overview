import sqlalchemy

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///onetomanyplain.db')


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet')

# backref creates a virtual coloumn owner which takes Person object
# we can do personobject.pets.name
# we can do petobject.owner.name


# pet table will get virtual coloumn called as owner
class Pet(db.Model):
    __tablename__ = "pet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer,db.ForeignKey('person.id'))

db.create_all()
piyush1=Person(name="piyush1")
db.add(Person(name="piyush1"))
db.add(Person(name="piyush2"))
db.commit()
db.add(Pet(name="spot1",owner_id=piyush1.id))
db.add(Pet(name="spot2",owner_id=piyush1.id))
print "wefwfe"
db.commit()


#
# db.add(Pet(name="spot4",owner=p1))
# db.add(Pet(name="spot5",owner=p1))
# db.add(Pet(name="spot6",owner=p1))p1

#print d
