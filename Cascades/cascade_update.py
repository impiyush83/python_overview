from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship, backref
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///cascades_update.db')


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(30))
    employee = relationship('Employee', backref='company',passive_updates=False)


class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    department_id = db.Column(Integer, ForeignKey('department.id',onupdate="cascade"))


db.create_all()

#working

object_to_be_updated = db.query(Department).filter_by(name="Comp").first()
object_to_be_updated.id = 22



db.commit()

#
#
# dc = Department(name="Comp")
# di=Department(name="It")
# db.add(dc)
# db.add(di)
# db.commit()
#
#
# emp1 = Employee(name="piyush", company=dc)
# emp2 = Employee(name="p1", company=di)
# emp3 = Employee(name="p2", company=di)
# emp4 = Employee(name="akshay", company=dc)
# db.add(emp2)
# db.add(emp3)
# db.add(emp4)
# db.add(emp1)
# db.commit()
#
# for i in  dc.employee:
#     print i.name , "in comp"
#
#
# for i in di.employee:
#     print i.name , "in iT"
#
#

# db.commit()
#
# d1=Department(name="Comp")
# d2=Department(name="IT")
#
# db.add(d1)
# db.add(d2)
# db.commit()
#
# e1=Employee(name="Akshay",company=d1)
# e2=Employee(name="Amit",company=d1)
# db.add(e1)
# db.add(e2)
# db.commit()
#
#
# for i in d1.employee:
#     print i.name, "IN COMP"
#
# for i in d2.employee:
#     print i.name, "IN IT"