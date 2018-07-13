from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///m1.db')


class Cars(db.Model):
    __tablename__ = 'cars'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    person_id = db.Column(Integer, ForeignKey('person.id'))
    car = relationship('Person', backref='own')


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)


db.create_all()

p1 = Person(name="Akshay")
p2 = Person(name="Piyush")

# db.add(p1)
# db.add(p2)
# db.commit()
# # db.rollback()

c1 = Cars(name="Swift", car=p2)
c2 = Cars(name="SwiftD", car=p2)
#
# db.add(c1)
# db.add(c2)
#
# db.commit()

res=db.query(Person).filter_by(name="Piyush").all()

res=res[0]
for i in res.own:
    print i.name