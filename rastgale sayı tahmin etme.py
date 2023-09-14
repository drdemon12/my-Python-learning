import random
a=random.randint(1, 10)

can=5
while can>0:
    can -= 1
    c=int(input("1 ile 10 arasında bir sayı giriniz: "))
    if a==c:
        print(f"Tebrikler doğru bildiniz değer {a}.Puanınız  {100-(20*(4-can))}")
        break
    elif c>a:
        print("girdiniz değer büyük.")
    else:
        print("girdiniz değer küçük.")

if can==0 and a==c:
    can=1
elif can==0 and a!=c :
    print(f"oyun bitti kaybettiniz değer {a} puanınız  {100-(20*(5-can))}")
