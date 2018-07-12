import sqlalchemy

from sqlalchemy import Column, Integer, ForeignKey, String, select, func
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
        return ' {}   {}'.format(self.roll_no,  self.name)
    #result = relationship("StudentCourse")
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

#qr = db.query(Student).select_from(StudentCourse).join(Student.roll_no).filter(Student.roll_no==StudentCourse.roll_no)
q1 = db.query(StudentCourse,Student).outerjoin(Student).all()
q2 = db.query(Student,StudentCourse).outerjoin(StudentCourse).all()
q3=q1.union(q2)


# result = db.query(StudentCourse.course_id,Student.name,Student.age).filter(Student.roll_no == StudentCourse.roll_no).all()

for i in q3:
    print i




