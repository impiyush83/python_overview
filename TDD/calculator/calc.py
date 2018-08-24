from calculator.db import db1
from calculator.models import User, Answers


class Eval1(object):

    def __init__(self, db1):
        self.db1 = db1


    def check_alpha_present(self,question):
        operators = ['+', '-', '/', '*']
        for i in question:
            if (ord(i) >= 65 and ord(i) < 91) or (ord(i) >= 97 and ord(i) < 123):
                return False
        return True

    def check_correct_expression(self, q):
        try:
            operators = ['+', '-', '/', '*']
            ll=q.split()
            if len(ll)==3:
                o1= ord(ll[0])
                o2=ord(ll[2])
                z= ll[1] in operators
                if  isinstance(o1,int) or isinstance(o1,float)  and isinstance(o2,int) or isinstance(o2,float)  and  z :
                    return True
            else:
                return False
        except:
            return False

    def enter_input(self, question):
        if self.check_alpha_present(question) and self.check_correct_expression(question):
            ll=question.split()
            return True
        return False

    def evaluate(self,question):
        answer=0
        if self.enter_input(question):
            ll = question.split()
            if ll[1]=='+':
                answer = int(ll[0]) + int(ll[2])
                var1 = User(question=question)
                self.db1.add(var1)
                var2 = Answers(answer=answer)
                self.db1.add(var2)
                db1.commit()
                return True
            elif ll[1]=='-':
                answer = int(ll[0]) - int(ll[2])
                var1 = User(question=question)
                self.db1.add(var1)
                var2 = Answers(answer=answer)
                self.db1.add(var2)
                db1.commit()
                return True
            elif ll[1] == '*':
                answer = int(ll[0]) * int(ll[2])
                var1 = User(question=question)
                self.db1.add(var1)
                var2 = Answers(answer=answer)
                self.db1.add(var2)
                db1.commit()
                return True
            elif ll[1] == '/' :
                answer = int(ll[0]) / int(ll[2])
                var1 = User(question=question)
                self.db1.add(var1)
                var2 = Answers(answer=answer)
                self.db1.add(var2)
                db1.commit()
                return True
            else:
                    return  False
        else:
            return  False

    def my_retrieved_obj(self, question):
        ll= self.db1.query(User.question).filter(User.question==question).all()
        if len(ll)==1:
            print "duuplicate ahe "
            return True
        else:
            return False

