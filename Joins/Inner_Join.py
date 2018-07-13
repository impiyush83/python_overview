import sqlalchemy

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///mydatabase.db')


class Student(db.Model):
    __tablename__ = "student"

    roll_no = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    address = db.Column(String)
    phone = db.Column(String)
    age = db.Column(Integer)

    def __repr__(self):
        return ' {}   {}'.format(self.roll_no, self.name)
    # result = relationship("StudentCourse")
    # , primaryjoin="and_(Student.roll_no==StudentCourse.roll_no,")


class StudentCourse(db.Model):
    __tablename__ = "studentcourse"

    id = db.Column(Integer, primary_key=True)
    course_id = db.Column(Integer)
    roll_no = db.Column(Integer, ForeignKey('student.roll_no'))
    stud = relationship('Student')

    def __repr__(self):
        return ' {}'.format(self.course_id)


# result = relationship("Student", primaryjoin="and_(Student.roll_no==StudentCourse.roll_no, ")


db.create_all()

u1 = Student(roll_no=4306, name="Akshay", address="Solapur", phone="78952146", age=21)
s1 = StudentCourse(id=44, course_id=4, roll_no=9)

db.add(u1)
db.add(s1)
db.commit()
#
# #result = db.query(StudentCourse,Student).outerjoin(Student).all()
#
# result= db.query(Student).join(StudentCourse).all()
#
# #result = db.query(StudentCourse.course_id,Student.name,Student.age).filter(Student.roll_no == StudentCourse.roll_no).all()
#
# for i in result:
#     print i
#
#
#
