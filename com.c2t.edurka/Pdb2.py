import pdb

class User:

    def __init__(self, runner):
        self.counter = runner

    def showSomething(self):
        for i in range(self.counter):
            pdb.set_trace()
            print(i)
        return

user = User(5)
user.showSomething()