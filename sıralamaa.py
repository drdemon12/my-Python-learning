x = int(input("Bir sayı giriniz: "))
y = int(input("Bir sayı giriniz: "))
z = int(input("Bir sayı giriniz: "))
result = x>y and x>z #x büyük
result1= y>z and y>x # y büyük
result2= z>x and z>y #z büyük
print(result==True )
print(result1==True )
print(result2==True )


import random
x = list(range(25))
random.shuffle(x)
print(x)

