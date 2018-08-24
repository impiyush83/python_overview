from sqlalchemy.exc import IntegrityError

from musicx.exceptions import UserInvalid, UserAlreadyExist
from musicx.models import User


class SignUp(object):

    def __init__(self, db):
        self.db = db

    def register_user(self, user_name, password):
        # type: (str,str) -> None
        if len(user_name) > 30 or len(password) > 30:
            raise UserInvalid()
        try:
            user = User(name=user_name, password=password)
            self.db.add(user)
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise UserAlreadyExist()

    def login(self, user_name, password):
        user = self.db.query(User).filter_by(name=user_name).all()
        if len(user)>0:
            for i in user:
                if i and i.password == password:
                    return True
            return False
        else:
            return False