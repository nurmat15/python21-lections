"==========PEREMENNYE=========="
# peremennye - eto ssylki na ya4eiki pamati, gde hranyatsya kakie-to dannye
a = 4

"==========vvod i vyvod dannyh==========="
# print - funkciya vyvoda dannyh v terminal
# input - funkciya vvoda dannyh s terminala
a = input()
print "vvedennoe 4islo", a, b, stringl"

"========4isla==========" 
# integers(int) - celye 4isla (5, 10, -35, 0, 1)
# float - vewestvennye ( s plavayuwei to4koi) (0.3, 0.345, 24.4785, -348.34875)
# decimal - to4noe vewestvennoe 4islo
# 4toby ispolzovat decimal nujno ego importirovat
from decimal import Decimal
c = Decimal(0.1)
# complex - komleksnye 4isla
complex(1, 5)

"======== Operacii nad 4islami========="
5 + 5 # slojenie
10 - 3 # vy4itanie
2 * 3 # umnojenie
15 / 3 # delenie (float 5.0)
15 / / 2 # celo4islennoe delenie(int 7)
5 ** 2 # vozvedenie v stepen
25 ** 0.5 # kvadratnyi koren 4isla

# modul 4isla - iz otricatelnogo 4isla sdelaet polojitelnoe |-5| = 5
abs (-5) # 5
abs(10) # 10
abs (-2.4) # 2.4

# pow:
# 1. vozvodit 4islo v opredelennuyu stepen
# 2. vozvrawaet ostatok ot deleniya rezultata 1 deistvie na tretie 4islo

pow(2, 3) # 8 = 2 ** 3
pow(2, 3, 4) # 8 % 4 = 0
# (2 ** 3)n% 4 = 0

# divmod - funkciya, kotoraya prinimaet 2 4isla i vozvrawayut 2 4isla, gde pervoe - eto celaya 4ast ot deleniya, a vtoroe - ostatok ot deleniya
vidmod(15, 2) # 7, 1
divmod(9, 3) # 3, 0
# round - funkciya, kotoraya okruglyaet 4islo
round(5.6) # 6
round(3.5) # 4
round(4.4) # 4
round(7.49) # 7 (beret pervoe 4islo posle to4ki)
# mojno ukazat skolko cifr posle zapyatoi ostavit
round(10.0475, 3) # 10.048
round(10.0474, 3) # 10.0447

# sqrt - funkciya dlya nahojdeniya kornya 4isla
# dlya raboty nujno ee impotirovat iz biblioteki math
from math import sqrt
sqrt(36) # 6
sqrt(25) # 5