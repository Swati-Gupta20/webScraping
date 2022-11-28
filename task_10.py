import json
with open('task_5.json','r')as f:
    s=json.load(f)
dl=[]
for i in s:
    if i['director'] not in dl:
        dl.append(i['director'])
d={}
for j in dl:
    l=[]
    for k in s:
        if k['director']==j:
            l.append(k['language'])
    d[j]=l
d1={}
for k in d:
    d2={}
    for l in range(len(d[k])):
        if d[k][l] not in d2:
            d2[d[k][l]]=d[k].count(d[k][l])
    d1[k]=d2
with open('task_10.json','w')as fi:
    json.dump(d1,fi,indent=4)

