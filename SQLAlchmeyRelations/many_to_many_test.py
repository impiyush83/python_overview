from sqlalchemy import String, Integer, ForeignKey, Table
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///manyTomany.db')

association_table = Table('association_table', db.metadata, db.Column('student_id', Integer, ForeignKey('student.id')),
                          db.Column('course_id', Integer, ForeignKey('course.id')))


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    courses = db.relationship("Course", secondary=association_table, lazy='dynamic')


class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    virtual_col = db.relationship('Student', secondary=association_table, lazy='dynamic')


db.create_all()
#
# s1 = Student(name="Akshay")
# s2 = Student(name="Piyush")
# s3 = Student(name="Amit")
# s4 = Student(name="Diksha")
# db.add(s1)
# db.add(s2)
# db.add(s3)
# db.add(s4)
# db.commit()
#
# c1 = Course(name="Java")
# c2 = Course(name="C++")
# c3 = Course(name="C")
# c4 = Course(name="Python")
# db.add(c1)
# db.add(c2)
# db.add(c3)
# db.add(c4)
# db.commit()
#
# c1.virtual_col.append(s1)
# c1.virtual_col.append(s2)
# c1.virtual_col.append(s3)
#
# c2.virtual_col.append(s1)
# c2.virtual_col.append(s2)
#
# db.commit()


