class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

b = B()
b.show()
b.display()

class C(B):
    def message(self):
        print("Class C")

c = C()
c.show()
c.display()
c.message()

class X:
    def method1(self):
        print("Class X")

class Y:
    def method2(self):
        print("Class Y")

class Z(X, Y):
    pass

z = Z()
z.method1()
z.method2()
