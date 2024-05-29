'''
types of inheritance : single A(B), multiple -> A(B, C), multilevel -> B(A) C(B).
'''


''' diamond problem -> if same method is implemented in both parent class then it will pick the method from the 
                       first parent class where that function was implemented (in this case B)

                       we can use method_resolution_order(mro) class_name.mro() to see in which order we will be looking for any method to execute
'''
class A:
    pass
    
class B(A):
    def f(self):
        return 1

class C(A):
    def f(self):
        return 2

class D(B, C):
    def f(self):
        return super().f()
    
d_obj = D()
print(d_obj.f())
print(D.mro())