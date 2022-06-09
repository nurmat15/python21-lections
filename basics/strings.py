"======stroki========"
# stroki - neizmenyaemyi tip dannyh, kotoryi prednazna4en dlya hraneniya teksta (posledovatelnosti simvolov), zaklu4ennogo v odinarnye ili dvoinye kavy4ki
# Sintaksis:
from distutils.log import error
from winreg import HKEY_LOCAL_MACHINE
string1 = 'stroka s odinarnym kavy4kami'
string2 = "stroka s dvoinym kavy4kami"
error = 'ne pravilnaya stroka'
string3 = "Don't" # vnutri dvoinyh kavy4ek vse odinarnye - prosto simvoly
string4 = '"Makers bootcamp"' # vnutri odinarnyh kavy4ek vse dvoinye - prosto simvoly
print(string3, string1, string2, string4)
string5 = ''' 
mnogostro4nyi tekst
v odinarnyh kavy4kah
Tut mojno stavit "lubye" 'kavy4ki' 
""""
'''
string6 = """ 

mnogostro4nyi tekst
v odinarnyh kavy4kah
Tut mojno stavit "lubye" 'kavy4ki'

"=========Ekranizaciya strok========"
# ekranizaciya spec-simvolov
'\n' # perenos na novuyu stroku
'\t' # tabulyaciya 
'\\' # otobrojenie \ (potomu 4to on yavlyaetsya instrukciei, kotoraya vliyaet na naw kod)
'\'' # otobrojenie '
"\"" # otobrojenie "
'\r' # vozvrawenie karetki v na4alo stroki
'\v' # perenos na novuyu stroku so smeweniem v pravo na dlinu predyduwei stroki

'hello\nworld'

# hello
# world

'hello\tworld'
# hello world

'4toby ekranizirovat nujen simvol \\'
# 4toby ekranizirovat nujen simvol \

'My website is Latracal \Solutin
# Solutiononte is Latracal

'hello\world'
# hello
#      world


"=========Formatirovanie strok=========="
title = 'Plov'
price = 1300
format1 = f'Nazvanie: {title}, Cena: {price}'
# Nazvanie: Plov, Cena: 1300

format2 = 'Nazvanie: %s, Cena: %s'
print (format2 % ("Gulyaw", "250"))
print (format2 % ("Samsy", "70")
 format3 = 'Nazvanie: {}, Cena: {}
 print(format3.format('Wakarap', '35'))


"========Metody strok======"
# metody tipov dannyh -funkcii, k kotorym my obrawaemsya 4erez to4ku
dir(str) # posmotret vse metody klassa (tipa dannyh)

'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'hello'.swapcase() # 'hELLO'
'hello'. title( $ 'Hello')
'hello world'.capitalize() # 'Hello world'
'hello'.center(11) # '  hello  '
'hello'. center(11,'-') # '--- hello---
'hello'.count('l') # 2
'hello'.count('ll') # 1
'hello hello'.count('hello') # 2
'hello'.count('w') # 0
'hello world'.startwith('hell') # True
'hello world'.startwith('H') # False
'hello world'.endwith('ld') # True

'hello world' .find(' ') # 5
'hello world'.find('o') # 4
'hello world'.find('wo') # 6
'hello world'.find('hello') # 0

'hello world'.split() # ['hello', 'world']
'hello world'.split('o') # ['hell','w', 'rld']
'$'.join(['hello world']) # 'hello$world'
' '.join(['hello', 'world']) # 'hello world'
''.join (['hello' 'world']) # 'helloworld'

"konketinaciya"
# eto skleivanie strok
'hello' + 'world' # 'helloworld
'hello' + '' + 'world # 'hello world'


"=========Indeksy========"
# indeks - poryadkovyi nomer simvola v stroke
'h e l l o  w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
string[0] # 'h'
string[10] # 'd'
string[5] # ' '

# srez - podstroka stroki
string[0:5] # 'hello'
string[0:6] # 'hello'
string[2:4] # 'll'
string[0:5][2:4] # 'll'

string[:5] # 'hello'
string[:6] # 'world'
string[:] # 'hello world'
string[0:11:2] # 'hlowrd'
string[::3] # 'hlwl'
string[::-1] # 'dlrow olleh'
string[::-2] # 'drwolh


"=====Dop infa===="
a = 5
b = 6
print (id(a))
print(id (b))
print(hash(a))



"""