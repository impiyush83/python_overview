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
# p1=Person(name="p1")
# db.add(p1)
# p2=Person(name="p2")
# db.add(p2)
# # p3=Person(name="p3")
# db.add(p3)
# db.commit()
#
# db.add(Pet(name="spot1",owner=p2))
# db.add(Pet(name="spot2",owner=p3))
# db.add(Pet(name="spot3",owner=p3))
# db.add(Pet(name="spot4",owner=p1))
# db.add(Pet(name="spot5",owner=p1))
# db.add(Pet(name="spot6",owner=p1))

p3 = db.query(Person).filter_by(name="p3").all()
print p3
for i in p3:
    for j in i.pets :
        print j.name

db.commit()

