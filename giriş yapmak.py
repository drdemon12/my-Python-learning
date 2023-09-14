kullanıcı_adı="demon"
sifre="123456"

girilen_kullanıcı_adı=input("Kullanıcı adınızı giriniz: ")
girilen_sifre=input("Şifrenizi giriniz: ")

result= girilen_kullanıcı_adı.lower().strip()==kullanıcı_adı and girilen_sifre.lower().strip()==sifre

print(f"Girilen kullanıcı adı veya şifreniz:{result}")