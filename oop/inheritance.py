"Nasledovanie - princip OOP, gde my mojem v do4ernem klasse unasledovat, peredopredelyat i ispolzovat vse attribyty i metody roditelskogo klassa"

class A:
    def method(self):
        print("metod in class A")

obj_a = A()        
obj_a.method() # 'metod in class A'

class B(A):
    """Nasledovali vse metody i attributy u klassa A"""

obj_b = B()
obj_b.method() # 'metod in class A'

"class A - roditelskii klass"
"class B - do4ernii klass"

class C(A):
    """Nasledovanie vse metody i attributy u klassa A i pereopredelili metod method"""

    def method(self):
        print("metod in class C")

obj_a = A()
obj_a.method() # 'method in class A'

obj_c = C()
obj_c.method() # 'method in class C'

"Pereopredelenie - daem to je nazvanie, no drugoe zna4enie"

"super() - funkciya kotoraya pozvolyaet obratitsya k roditelskomu klassu i vyzvat opredelennye metody i attribyty"
class A:
    def range(self,n):
        return list(range(0,n+1))

class B(A):
    def range(self):
        # 4erez super my obrawaemsya k metodu roditelskogo klassa
        return A.my_range(10)        
obj_a = A()
obj_a.my_range(3) # [0, 1, 2, 3,]

obj_a = B()
obj_a.my_range() # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"==========Vidy nasledovaniya============="
# odino4noe nasledovanie
# mnojestvennoe nasledovanie
# mnogouravnevoe nasledovanie
# ierarhi4eskoe nasledovanie
# gibridnoe nasledovanie


