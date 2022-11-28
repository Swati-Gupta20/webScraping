# import requests
# url="https://www.imdb.com/india/top-rated-indian-movies/"
# sample=requests.get(url)
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(sample.text,"html.parser")
# title=soup.title
# print(title)
l=["http://www.imdb.com/title/tt0259534/"]

id=l[0][-10:-1]
print(id)