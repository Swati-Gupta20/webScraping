from bs4 import BeautifulSoup
import requests
import json
url=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
x=url.json
soup=BeautifulSoup(url.text,"html.parser")
# print(soup)
def scrap_top_list():
    main_div=soup.find('div',class_='lister')
    tbody=main_div.find('tbody',class_='lister-list')
    trs=tbody.find_all('tr')
    
    movieRank=[]
    movieName=[]
    releaseYear=[]
    movieUrl=[]
    movieRatings=[]
    for tr in trs:
        position=tr.find('td',class_='titleColumn').get_text().strip()
        rank=''
        for i in position:
            if '.' not in i:
                rank+=i
            else:
                break
        movieRank.append(rank)
        title=tr.find('td',class_='titleColumn').a.get_text()
        movieName.append(title)
        year=tr.find('td',class_='titleColumn').span.get_text()
        releaseYear.append(year)
        rating=tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
        movieRatings.append(rating)
        link=tr.find('td',class_='titleColumn').a['href']
        movieLink='https://www.imdb.com'+link
        movieUrl.append(movieLink)
    topMovies=[]
    details={'position':'','name':'','year':'','rating':'','url':''}
    for i in range(0,len(movieRank)):
        details['position']=int(movieRank[i])
        details['name']=str(movieName[i])
        releaseYear[i]=releaseYear[i][1:5]
        details['year']=int(releaseYear[i])
        details['rating']=float(movieRatings[i])
        details['url']=str(movieUrl[i])
        topMovies.append(details)
        details={'position':'','name':'','year':'','rating':'','url':''}
    with open('web.json','w') as f:
        json.dump(topMovies,f,indent=4) 

scrap_top_list()





