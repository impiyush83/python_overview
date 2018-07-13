import sqlalchemy

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///onetomany.db')


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet',backref='owner')

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
#
p1 = db.query(Person).filter_by(name="p").first()
for i in p1.pets:
    print i.name

spot4= db.query(Pet).filter_by(name="spot4").first()
print spot4.owner.name

#
# db.add(Pet(name="spot4",owner=p1))
# db.add(Pet(name="spot5",owner=p1))
# db.add(Pet(name="spot6",owner=p1))p1

#print d
