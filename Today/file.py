from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///:memory:')


class Parent(db.Model):
    __tablename__ = 'parent'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(20))


class Child(db.Model):
    __tablename__ = "child"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    child_attr = db.Column(String(20))
    parent = relationship('Parent')


db.create_all()

p1 = Parent(name="Akshay")
db.add(p1)

c1 = Child(child_attr="Child1")
c1.parent_id = p1.id
db.add(c1)


p2 = Parent(name="Piyush")
db.add(p2)

c2 = Child(child_attr="Child2")
c2.parent_id = p2.id
db.add(c2)
for user in db.query(Parent):
    print user.name, '\t', user.id

for user in db.query(Child):
    print user.id, user.parent_id, user.child_attr
db.commit()

