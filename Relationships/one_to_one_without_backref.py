import sqlalchemy

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///o2o.db')


class Life(db.Model):
    __tablename__ = "life"
    id = db.Column(db.Integer, primary_key=True)
    personify = db.relationship('Person',uselist=False)


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer)
    life_id = db.Column(db.Integer, ForeignKey("life.id"),unique=True)
    name = db.Column(db.String(20) , primary_key =True )
    lifify = db.relationship('Life')

db.create_all()


l1=Life()
l2=Life()
db.add(l1)
db.add(l2)
db.commit()

l1 = db.query(Life).filter_by(id=1).first()

p1 = Person(id=1, name="n1",lifify=l1)
db.add(p1)
db.commit()
p2=Person(id=1,name="m12",lifify=l1)
db.add(p2)
db.commit()

print l1.personify.name
