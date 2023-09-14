a = ["a","b","c","d","f"]
b = a[-1:] #son satırsakini ekler
a = a+ b
del a[-1] # son satırdakini siler
a=a[::-1] #tersten yazar
print(a)

import random
c = random.choice(a)
c=list(c)
print(c)