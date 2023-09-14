a="sEn hAyıRdıR oGlum."
a=a.title()   # her kelimenin baş harfi büyük
a=a.capitalize() #sadece ilk harf büyük
a=a.upper() #hepsini büyük yapar
a=a.count("r") # r leri sayar
b="sEn" in a # kelimeyi arar
a=a.split(.) #cümleleri noktaya göre ayırıyor.
#---------------------------
a=a.split()
a="_".join(a) #ayrı kelimeli birleştirir.
#------------------------------
a=a.replace("sEn","ben") #eski,yeni şeklinde yazılır.
a=a.center(35,"*")
print(a)