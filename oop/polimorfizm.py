"=======Polimorfizm========"
# Polimorfizm - princip OOP, v kotorom metody v raznyh klassah nazyvayutsya odinakovo. ( odin interfeis - raznyi funkcional)

class Dog:
    def speak(self):
        print('gaf-gaf')

class Cat:
    def speak(self):
        print('myau-myau')

class Frog:
    def speak(self):
        print('kva-kva')    

animals = [Cat(), Dog(), Cat(), Frog(), Frog()]       

for animal in animals:
    animal.speak()

    print (dir(str))
    print (dir(list))
    print (dir(dict))
    print (dir(int))

# __len__    
"sdfghj" == 6
[]