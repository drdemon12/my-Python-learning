liste = ["1","2","5a","10b","abc","10","50"]

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue 

while True:
    sonuc = input("bir sayı giriniz: ")
    if sonuc== "n" :
        break
    try:
        b = float(sonuc)
        print("girdiğiniz sayı: ", b)
    except ValueError:
        print("geçersiz değer girdiniz.")
        continue

karakter = "şçğüıİ"
parola = input("parola giriniz: ")

for i in karakter:
    if i in parola:
        raise TypeError("türkçe karakter içeremez.")
    else:
        pass
print("parola oluşturulmuştur.")