"========Slovari======"
# Slovar (dict) - izmenyaemyi, iteriruemyi,neindesiruemyi,neuporyado4ennyi, tip dannyh, v kotorom zna4eniya hranyatsya v parah ( klu4 : zna4enie)

{"a":1, "b":2, "c":3}
print(dict_["a"]) # Hello

# klu4ami v slovare mogut yavlyatsya vse nrizmenyaemye tipy dannyh
# zna4enie v slovare mogut yav;yatsya lubye tipy dannyh
# klu4i doljny byt unikalnymi

dict_ = {
    1:"hello",
    "a":4,
    4.5: {"a":5},
    # {"s":5}: 44 # TypeError: unhashable type: 'dict'
}

print(dict_[4.5]) # {"a":5}
print(dict_[4.5]["a"]) # 5
print{dict_["a"]} # KeyError: "a"

"=============Создание словарей================"
dict1 = {"a":3}
dict2 = dict( [ ('key1', 'value1'), ('key2', 'value2') ] )
# dict2 = {'key1':'value1', 'key2':'value2'}
dict3 = dict( ( ['key1', 'value1'], ('key2', 'value2') ) )
# dict3 = {'key1':'value1', 'key2':'value2'}
dict4 = dict(['ab', 'cd', 'de'])
# dict4 = {"a":"b", 'c':'d', 'd':'e'}
key1, value1 = 'ab'
dict4[key1] = value1
key2, value2 = 'cd'
dict4[key2] = value2
key3, value3 = 'de'
dict4[key3] = value3


dict5 = dict(['abc']) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
key1, value1 = 'abc' #
dict5[key1] = value1

"=======Metody slovarya========"
dict_.clear() # 4istit slovar
    print(dict_) # {}

dict_ = dict.fromkeys([1,2,4])
print(dict_) # {1:None, 2:None, 4:None}

dict_ = dict.fromkeys([1,2,4]), "hello"
print(dict_) # {1:"hello", 2:"hello",4:"hello"}

dict_ = dict.fromkeys([1,2,4])
print(dict_) # {1:"None",2:"None",4:"None"}

dict_ = dict.fromkeys([1,2,4]), "hello"
print(dict_) # {1:"hello", 2:"hello", 4:"hello"}
dict_ = {"a":1, "b":2}
dict_["a"] # 1
dict_["c"] # KeyError

# metod get nujen tolko dlya polu4enii zna4enii
dict_.get("a") # 1
dict_.get("c") # None
dict_.get("c",5) # 5
dict_.get("a", 5) # 1

dict_.keys() # dict_keys(['a'],['b'])
dict.values() # dict_values ([1,2])
dict_.items() # dict_items([('a', 1), ('b', 2)])

dict1 = {1;"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
dict1.update(dict2)
print(dict1) # {1:"a", 2:"b", 3:"d", 4:"e"}
print(dict2) # {3:"d", 4:"e"}

# metod update dobavlyaet pary iz vtorogo slovarya v pervyi
print(dict1.pop(3)) # d
print(dict1) 
3 {3:"d", 4:"e"}

# metod pop udalyaet paru po klu4yu i vozvrawaet zna4enie
popped # dict1.pop(3)
print(dict1)#(3:"d", 4:"e")
print (dict2) # {3:"d", 4:"e"}

# metod popitem udalyaet i vozvrawaet poslednyuyu paru
popped = dict.pop (3)
print(dict1) # {1:"a", 2:"b", 4:"e"}
print popped # d

print(dict1.popitem())
print(dict1)







