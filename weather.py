import requests
import urllib.parse
from bs4 import BeautifulSoup
import html
city = str(input("Введите город: "))
safe_string = urllib.parse.quote_plus(city)
a=requests.get(f"https://www.google.com/search?hl=ru-RU&ie=UTF-8&source=android-browser&q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F+{safe_string}&client=ms-android-xiaomi-rev1").text
soup = BeautifulSoup(a ,"html.parser")
today = soup.findAll('div', class_='BNeawe tAd8D AP7Wnd')
now = soup.findAll('div', class_='BNeawe iBp4i AP7Wnd')
print("Сегодня: "+today[0].text)
print("Сейчас: "+now[0].text)
