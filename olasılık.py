
numbers = [ ]
numbers = [x**3 for x in range(5,15) if x%2==0] #5den 25 e kadar olan çift sayıların küpü
print(numbers)

ages=[]
years = [1969, 1971, 1997, 2000]
ages = [2020-x for x in years]
print(ages)

result = [] # bütün olasılıkları yazar 5,12,8 in kombinasyonu
for i in range(5):
    for j in range(12):
            for k in range(8):
                 result.append((i,j,k))
print(result)