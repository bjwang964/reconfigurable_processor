class conf():
    def __init__(self):
        self.c = 9

class A():
    def __init__(self):
        self.c = conf()
    def p(self):
        print(self.c.c)

class B():
    def __init__(self):
        self.A = A()
    def update(self):
        self.c = conf()
        self.c.c = 1
        self.A.c = self.c
        self.A.p()




b = B()
b.update()
