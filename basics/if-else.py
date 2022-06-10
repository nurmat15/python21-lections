"========Logi4eskie operatory======"
#logi4eskie operatory - vyrajenie,kotorye vozvrawayut True, esli pravda, false - esli loj

5 == 5 # True
4 == 5 # False

5 != 5 # False
5 != 2 # True

5 > 10 # False
10 > 5 # True
5 > 5 # False

5 < 10 # True
10 < 5 # False
5 < 5 # False

5 <= 10 # True
10 <= 5 # False
5 <= 5 # True

5 >= 10 # False
10 >= 5 # True
5 >= 5 # True
 
 "5" = 5 # False tak kak pervoya stroka a vtoroe 4islo

 "=========Bool type============"
# bulevyi tip dannyh - imeet 2 zna4eniya True,False
bool(1) # True
bool(0) # False tolko 0 budet davat False
bool(-277) # True

bool('hello') # True
bool(") # False
bool('') # True tak kak zdes est probel

bool(True) # True
bool(False) # False

"========None Type========"
# None - tip dannyh s odnim zna4eniem None, kotoryi ispolzuetsya dlya obozna4eniya pustyh zna4enii ili otsutstvie zna4eniya
bool(None) # False
bool('None') # True tak kak vnutri stroka

a = None
print(bool(a)) # False tak kak a = None
print(a is None) # True tak kak is eto proverka na polnoe sootvetstvie
# is proveryaet ya4eiki pamyati

"=======Uslovnye operatory======="
# uslovnye opratory nujny dlya togo 4toby pri raznyh vhodnyh danyh kod rabotal po raznomu
if uslovie1 :
    telo1
# budet rabotat tolko esli uslovie1 verno
if uslovie1
telo1
else:
    telo2
    if uslovie1:
        telo1
        elif uslovie2:
            telo2
            else:
                telo3

# v odnoi konstrukcii my mojem ispolzovat neograni4ennoe kol-vo elif
# v odnoi konstrukcii my mojem ispolzovat tolko odin if
# else my tak-je mojem ispolzovat tolko odin raz ili ne ukazyvat voobwe

a = int(input('Vvedite 4islo'))
if a > 0:
    print(f'4islo {a} - polojitelnoe')
    elif a < 0:
        print(f'4islo {a} - otricatelnoe')
        else a = 0:
        print (f'4islo{a} - eto 0')

"=======FizzBuzz======="
# esli 4islo kratno 3 - vyvesti Fizz
# esli 4islo kratno 5 - vyvesti Buzz
# esli 4islo kratno i 5 i 3 - vyvesti FizzBuzz
# esli 4islo ne kratno ni 5 ni 3 - vyvesti 4islo

for i in range(1, 101):
    if i % 3 == 0
    print ("Fizz")
    if i % 5 == o
    print ("Buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        else: print(i)

