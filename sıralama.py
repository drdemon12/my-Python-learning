b=[1,2,45,5,8,9,11,25,64]
c=["j","k","h","f","j"]
#b[3] = 3111 #düzenleme
#b.append(99) #ekleme
#b.append("hi")
b.insert(0,5) # 0dan önceki elemana 5 sayısını ekler
#b.pop(1) #silme işlemi yapar
#b = min(b)
#b = max(b)
b.sort() #küçükten büyüğe sıralama
b.reverse() #büyükten küçüğe çevirme
c.sort() #alfabetik sıralama
b,c= c,b  #c ile b nin içerisindekileri değiştirir
b.clear() #hepsini siler
print(b)