a = "DEMON"
a=a.center(45,"_")
a=a.replace(""," ")

liste = [a,"a"]

while True:
    try:
        b = next(iter(liste))
        print(b)
    except StopIteration:
        break
SONSUZA KADAR TEKRARLIYOR VE KAPATINCA DONUYOR

-------------------------------------------------------------------

liste1 = ["ali","ayşe", "fatma"]
c = iter(liste1)
while True:
    try:
        b = next(c)
        print(b)
    except StopIteration:
        break


generator = (a**5 for a in range(100))
print(generator)
for c in generator:
    print(c)
#sıfırdan yüze kadar her sayının 5. kuvvetini alır