import sqlalchemy

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///m2o.db')

#db.add(Pet(name="spot6",owner=p1))
class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    employee = db.relationship('Employee',backref='companies')


# backref creates a virtual coloumn owner which takes Person object
# we can do personobject.pets.name
# we can do petobject.owner.name


# pet table will get virtual coloumn called as owner
class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))



db.create_all()


# e1=Employee(name="piyu")
# e2=Employee(name="siyu")
# e3=Employee(name="hiyu")
# e4=Employee(name="oiyu")
# db.add(e1)
# db.add(e2)
# db.add(e3)
# db.add(e4)
# db.commit()
#
#
# c1= Company(name="hsbc",employee=e1)
# c2=Company(name="barclays",employee=e1)
# db.add(c1)
# db.add(c2)
# db.commit()

c1 = db.query(Company).filter_by(name="hsbc").first()

c2 = db.query(Company).filter_by(name="barclays").first()
print c2.employee.name
print c1.employee.name

e1 = db.query(Employee).filter_by(name="piyu").first()
for i in e1.companies:
    print i.name