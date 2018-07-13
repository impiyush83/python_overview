from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///manyTomany.db')


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    courses = db.relationship("Course")


class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    course_id = db.Column(Integer, ForeignKey('student.id'))
    student = db.relationship('Student')


db.create_all()

# s1=Student(name="Akshay")
s2=Student(name="Piyush")
# db.add(s1)
# db.add(s2)
# db.commit()
#
# c1=Course(name="C++",student=s1)
# db.add(c1)
# db.commit()
#
c2=Course(name="Java",student=s2)
#
db.add(c2)
db.commit()
#
# c3=Course(name="Python",student=s2)
# db.add(c3)
# db.commit()
#
# c4=Course(name="Django",student=s2)
#
# db.add(c4)
# db.commit()

res=db.query(Student).filter_by(name="Piyush").first()
for i in res.courses:
    print i.name



