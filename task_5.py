import json
import requests
from bs4 import BeautifulSoup
def scrap_movie_details():
    with open('task_1.json','r') as f:
        d=json.load(f)
    url=[]
    for i in range(len(d)):
        url.append(d[i]['url'])
    list=[]
    urls=url
    for c in urls:
        x=requests.get(c)
        soup=BeautifulSoup(x.text,'html.parser')
        movieDetails=soup.find('script',type='application/ld+json').text
        lang=soup.find("li",attrs={"data-testid":"title-details-languages"}).a.get_text()
        s=json.loads(movieDetails)
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
        list.append(dic)
    
    with open('task_5.json','w') as k:
        json.dump(list,k,indent=4)
scrap_movie_details()



# with open('task_5.json','r')as k:
#         a=json.load(k)
# print(a['movies'])
