"=========Tuple======"
# kortej, neizmenyaemyi,indexiruemyi,uporyado4ennyi,iteriruemyi tip dannyh,prednazna4ennyi dlya hraneniya lubyh dannyh v opredelennom poryadke
# (v celom ne otli4aetysa ot spiskov, prosto ne izmenyaemyi,poetomu zanimaet menwe pamyati)

tuple1 = (1,2,3) # (1,2,3)
tuple2 = ('hello', 2.5, 19, (2,3), [1,2,3])
tuple3 = tuple('hello') # ('h','e','l','l','o')

tuple4 = 1,2,3 # (1,2,3)
tuple5 = (5) # 5 (int)
tuple6 = 5, # (5,)
tuple7 = 'hello',

list_ = [1,2,1,4,1,5,1,7,2,4,4]
list_.count(1) # 4
list_.count(2) # 2
list_.count(4) # 3

list_ = ['hello', 'hello', 'hello']
list_.count('h') # 0
list_.count('hello') # 3
len(list_) # 3
