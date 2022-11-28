import json
import requests
from bs4 import BeautifulSoup
def scrap_movie_details():
    with open('task_1.json','r') as f:
        d=json.load(f)
    url=[]
    for i in range(len(d)):
        print(i+1,':',d[i]['name'])
        url.append(d[i]['url'])
    user=int(input('select movie sl no.:'))-1
    x=requests.get(url[user])
    soup=BeautifulSoup(x.text,'html.parser')
    movieDetails=soup.find('script',type='application/ld+json').text
    data=json.loads(movieDetails)
    with open('task_9.json','w')as f:
        json.dump(data,f,indent=5)
scrap_movie_details()