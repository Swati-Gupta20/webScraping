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
    lang=soup.find("li",attrs={"data-testid":"title-details-languages"}).a.get_text()

    data=json.loads(movieDetails)
    with open('try.json','w')as f:
        json.dump(data,f,indent=4)
    with open('try.json','r')as fi:
        s=json.load(fi)
    dic={}
    for j in s:
        time=s['duration'][2:]
        dic['name']=s['name']
        dic['director']=s['director'][0]['name']
        dic['image']=s['image']
        dic['description']=s['description']
        dic['language']=lang
        dic['gener']=s['genre']
        dic['duration']=[time[:2]+' '+time[2:]]
        dic['country']='India'
    with open('task_4.json','w') as k:
        json.dump(dic,k,indent=4)
scrap_movie_details()


