"======Comprehension========"
# comprehension - generaciya posledovatelnostei v odnu stroku ispolzuya cykl

# 1. deistvie for element in iteriruemyi obiekt 
# 2. deistvie for element in iteriruemyi obiekt if filter 

"=======List comprehension========"
"sozdat spisok sostoyawii iz 4isel ot 1 do 10 umnojennyh na 2"
list_ = []
for i in range(1, 11):
    list_.append(i)
# list_ = [1,2,3,4,5,6,7,8,9,10]

list_ = list( (i*2 for i in range(1,11)) )
# list_ = [1,4,6,8,10,12,14,16,18,20]

list_ = [i*2 for i in range(1,11)]
# list_ = [1,4,6,8,10,12,14,16,18,20]

"sozdat spisok sostoyawii iz 4etnyh 4isel ot 1 do 10"
list_ = []
for i in range(1,11):
    # if not 0 (4etnoe)
    if not i % 2:
        list_.append(i)

        list_ = [i for i in range(1,11) if not i%2]

list_ = [i for i in range(1,11,2)]

# list_ = [2,4,6,8,10]

list_ = [print(i) for i in range(10)]
# [None,None,None,None,None,None,None,None,None,None]
list_ = ["hello" for i in range(10)]
#["hello", "hello", "hello", "hello", "hello","hello", "hello", "hello", "hello","hello"]

print([input()for i in range(10)])
# na kajdoi iteracii zaprawivaet input

"sozdat spisok sostoyawii iz 4isel ot 1 do 10, no vmesto 4isel napisat'4etnoe' ili ' ne 4etnoe'"

list_ = [ 'ne4etnoe' if i % 2 else '4etnoe' for i in range(1,11) ]
#['ne4etnoe' '4etnoe', 'ne4etnoe', '4etnoe']


list1 = [1,'hello', 3, 'a', 4, 6, 8 'hw']

# "sozdat spisok iz 4isel nahodyawihsya v list1, zameniv ih na '4etnoe' ili 'ne4etnoe'""
list_ = [ ' ne4etnoe' if i % 2 else '4etnoe' for i in list if type(i) == int or type(i)] == float

"=======Dict coprehension=========="
# sozdat slovar , gde klu4i - 4isla ot 1 do 10, a zna4enie eti 4isla vvide stroki
dict_ = dict( ( i, str(i)) for i in range(1,11) )




'dany 2 spiska, sozdaite slovar, gde klu4i - elementy 1 spiska, a zna4enie - vtorogo'
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
dict_ = dict (((list1[index], list2[index])for index in range(len(list))))
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

'sozdaite kopiyu slovarya'
dict1 = {"a":1, "b":2, 4:"c"}
dict2 = { key: value for key, valuein dict1.items() }
'pomenyaite klu4 i zna4enie mestami'
'dan slovar, gdezna4eniya - spisok s 4islami, sozdaite novyi slovar, gde zna4eniya - summa etih 4isel'
dict1 = {
    "a":[1,2,3,4,5],
    "b":[10,30,2,5],
    "c":[74,28,47],
    "d":[4,6,2,92,9]
}
dict2 = { key: sum(value for key, value in dict1.items()) }
# {'a':15, 'b': 47, 'c': 149, 'd': 113}

"========Vlojennye comprehension============"
'sozdaite slovar, gde klu4ami budut 4isla ot 1 do 10, a zna4eniya budut spiski ot 1 do 4isla(kotoryi klu4)'

dict_ = {i: list(range(1, i+1))for i in range(1,6) }
    


