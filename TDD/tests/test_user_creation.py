import pytest
from hamcrest import *


#from musicx.db import db
from calculator import calc
from calculator.calc import Eval1
from calculator.db import db1
from calculator.models import User
from musicx.exceptions import UserInvalid, UserAlreadyExist
#from musicx.models import User, Address
from musicx.signup import SignUp

"""

class TestUserCreation(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        db.create_all()

    @staticmethod
    def _test_user_can_be_created():
        amit = User(name="amit", password="1234")
        db.add(amit)
        db.commit()

        users = db.query(User).all()
        amit_user= users[0]

        address = Address()
        address.city_name = "Pune"
        address.user_id= amit_user.id

        db.add(address)
        db.commit()

        assert_that(amit_user.address[0].city_name, is_("Pune"))
        assert_that(address.user, is_(amit_user))
        assert len(users) is 1

    def _test_user_can_not_register_if_user_name_is_greater_than_30_chars(self):
        signup = SignUp(db)
        assert_that(calling(signup.register_user).with_args("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq", "1234"),
                    raises(UserInvalid))

    def _test_user_can_register_if_details_are_correct(self):
        signup = SignUp(db)
        signup.register_user("amit", "1234")

        users = db.query(User).all()
        assert len(users) is 1


    def _test_duplicate_user_can_not_exist(self):
        signup = SignUp(db)
        signup.register_user("amit", "1234")

        users = db.query(User).filter_by(name='amit').all()
        assert len(users) is 1
        assert_that(calling(signup.register_user).with_args("amit", "4333"), raises(UserAlreadyExist))

    def _test_user_can_login(self):
        signup = SignUp(db)
        signup.register_user("amit", "1234")

        result = signup.login("amit", "1234")
        assert_that(result, is_(True))



    def _test_user_login_if_user_not_exist(self):
        signup = SignUp(db)
        result = signup.login("ppp", "1234")
        assert_that(result, is_(False))


"""

class TestCalcWorking(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        db1.create_all()

    def _test_alpha_char(self):
        eval = Eval1(db1)
        operands = eval.check_alpha_present("2.0 + 2 + 4 + a")
        assert_that(operands, is_(True))



    def _test_check_the_no_of_operands(self):
        eval = Eval1(db1)
        operands = eval.check_correct_expression("2 + 2")
        assert_that(operands,is_( True))



    def _test_check_the_question(self):
        eval = Eval1(db1)
        operands = eval.enter_input("2 + 2")
        assert_that(operands,is_( True))


    def _test_answer(self):
        eval=Eval1(db1)
        operands=eval.evaluate("2 + 5")
        assert_that(operands,is_(True))

    def test_check_duplicacy_of_question(self):
        eval= Eval1(db1)
        #my_question = User(question="2 + 2")
        obj1=eval.my_retrieved_obj("2 + 3")
        assert_that (obj1,is_(True))
        #assert_that(is_(True),obj1)