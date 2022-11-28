import json
import requests
from bs4 import BeautifulSoup
import os

with open('task_1.json','r')as f:
    s1=json.load(f)
l=[]
n=1
for i in s1:
    if i['url'] not in l:
        l.append(i['url'])
        print(n,':',i['name'])
        n+=1
a=int(input('choose movie sl no.: '))-1
id=l[a][-10:-1]
file=id+'.json'
x=requests.get(l[a])
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
with open(file,'w') as k:
        json.dump(dic,k,indent=4)
l2=[]
n1=1
for i in s1:
    a=i['url']
    if a[-10:-1] not in l2:
        l2.append(a[-10:-1])
    print(n1,':',a[-10:-1])
    n1+=1
a1=int(input('check id:'))-1
fileName=l2[a1]+'.json'
path='/home/navgurukul/Desktop/Python2/web-scrapping/'

if os.path.exists(path+fileName): 
    print('file exists')   
    with open(fileName,'r')as f:
        q=json.load(f)
    print(q)
else:
    print('scraped from IMDB')
    x=requests.get(l[a1])
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
    with open(fileName,'w') as k:
        json.dump(dic,k,indent=4)
    with open(fileName,'r')as f3:
        o=json.load(f3)
    print(o)


