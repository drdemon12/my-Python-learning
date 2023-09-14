import requests
import json

aa=(f"US Dollar (USD),\nCanadian Dollar (CAD),\nAustralian Dollar (AUD),\nArgentine Peso (ARS),\nBritish Pound (GBP),\nEuro (EUR),\nTurkish Lira (TRY),")
print(aa)
d = str(input("bozduracağınız para birimini giriniz "))
c = str(input("alacağınız para birimini giriniz: "))
f = float(input(f"ne kadar {d} bozdurmak istiyorsunuz?  "))

b = requests.get(f"https://api.exchangeratesapi.io/latest?base={d}")
b = json.loads(b.text)

kurlar = b["rates"][c]
abc = float(kurlar)

print(f"1 {d} = {abc} {c}")
print(f*abc)
 

