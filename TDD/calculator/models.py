from sqlalchemy import String, Float
from calculator.db import db1


class User(db1.Model):
    __tablename__ = "user"
    question = db1.Column(String(100), primary_key=True)


class Answers(db1.Model):
    __tablename__ = "answer"
    answer = db1.Column(Float, primary_key=True)
