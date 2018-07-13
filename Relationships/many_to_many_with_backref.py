
import sqlalchemy

from sqlalchemy import Column, Integer, ForeignKey, String,Table
from sqlalchemy.orm import relationship

from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///m2m.db')

association_table= db.Table('association_table', db.Column('left_id', Integer, ForeignKey('left.id')),db.Column('right_id', Integer, ForeignKey('right.id')))


class Parent(db.Model):
    __tablename__ = 'left'
    id = db.Column(Integer, primary_key=True)
    children = db.relationship("Child",secondary=association_table,backref=db.backref('guardians',lazy='dynamic'))

class Child(db.Model):
    __tablename__ = 'right'
    id = db.Column(Integer, primary_key=True)


db.create_all()


p1= Parent()
p2=Parent()
p3=Parent()
p4=Parent()
db.add(p1)
db.add(p2)
db.add(p3)
db.add(p4)
db.commit()


c1= Child()
c2= Child()
c3= Child()
c4= Child()
db.add(c1)
db.add(c2)
db.add(c3)
db.add(c4)
db.commit()


c1.guardians.append(p1)
c1.guardians.append(p2)
c1.guardians.append(p3)
c1.guardians.append(p4)

c2.guardians.append(p1)
c2.guardians.append(p2)


db.commit()

