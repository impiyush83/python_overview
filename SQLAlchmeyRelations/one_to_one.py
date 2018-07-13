from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///OneToOne.db')


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    mobile1 = db.relationship("Mobile", uselist=False)


class Mobile(db.Model):
    __tablename__ = 'mobile'
    id = db.Column(Integer, primary_key=True)
    name=db.Column(String)
    person_id = db.Column(Integer, ForeignKey('person.id'), unique=True)
    person = db.relationship('Person')


db.create_all()

p1=Person(id=1, name="Akshay")
p2 = Person(id=2, name="Piyush")
db.add(p1)
db.add(p2)
db.commit()

m1=Mobile(id=1, name="Moto", person=p1)
m2=Mobile(id=2, name="1+6", person=p2)
db.add(m1)
db.add(m2)
db.commit()


