'''
Polymorphism : types -> Compile Time (Static Binding) and Runtime (Dynamic Binding)

Compile Time -> The stage where the source code is converted to bytecode, and syntax errors are detected.
                what happens during compile is bytecode compilation, syntax checking, static analysis

Runtime -> The stage where the bytecode is executed, and the program's dynamic behavior is realized.
           This is when the actual execution of the code occurs, and all dynamic behavior is handled.
           what happens during runtime is execution flow, runtime errors(zerodivision error)
'''

'''
compile time polymorphism : during compile time we will be able to find this error

def f(a):
    print(a)

def f(a, b):
    print(a + b)

f(10)
'''

'''
runtime polymorphism : during runtime we will be able to identify which method will execute for an object

from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def f(self):
        pass

class B(A):
    def f(self):
        print(10)
        return

class C(A):
    def f(self):
        print(20)
        return

b_obj = B()
c_obj = C()

b_obj.f()
c_obj.f()
'''