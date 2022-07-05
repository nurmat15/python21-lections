"===================Принципы ООП======================"
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация

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


