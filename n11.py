import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/masaustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li",{"class":"column"},limit=50)

for li in list:
    title = li.a.get("title")
    link = li.a.get("href")
    eskipara = li.find("div",{"class":"proDetail"}).find("a",{"class":"oldPrice"}).text.strip()
    yenipara = li.find("div",{"class":"proDetail"}).find("a",{"class":"newPrice"}).text.strip()

    print(f"adı: {title} linki: {link}  eskipara: {eskipara}      to     yenipara: {yenipara}")