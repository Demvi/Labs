import requests
from bs4 import BeautifulSoup as bs
import os,webbrowser


user_teg = str(input("Введите тег аккаунта истаграмм: @"))

url = "https://apkun.com/search?query=" + user_teg
#api.instagram.com/oembed/?url="ссылка на фото   --- Если есть впн "

r = requests.get(url)
soup = bs(r.text, "html.parser")


spImg = soup.find('img', class_='img-fluid w-100')

spImg = spImg["src"]


#Если профиль закрыт, то ничего не выдаст

print(spImg)

webbrowser.open(str(spImg))

