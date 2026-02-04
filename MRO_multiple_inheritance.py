class A:
    def show(self):
        print("A.show")
class B(A):
    def show(self):
        print("B.show")
        super().show()
class C(A):
    def show(self):
        print("C.show")
        super().show()
class D(B,C):
    def show(self):
        print("D.show")
        super().show()
d=D()
d.show()
print(D.mro())