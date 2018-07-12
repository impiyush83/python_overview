from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import PasswordType

from musicx.db import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=30), unique=True)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512','md5_crypt']))


class Address(db.Model):
    __tablename__ = "address"

    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="address")
    city_name =  db.Column(String(length=30))