class A:
    def do_work(self):
        pass

class B:
    def do_stuff(self):
        pass

class C(A):
    pass

class D(B):
    pass

class E(D):
    pass

a = E()
print(type(D))