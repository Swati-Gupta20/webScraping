import json

with open('task_5.json','r')as f:
    s=json.load(f)

l=[]
for i in s:
    if i['director'] not in l:
        l.append(i['director'])
dic={}
for j in l:
    c=0
    for k in s:
        if k['director']==j:
            c+=1
    dic[j]=c
with open('task_7.json','w')as f:
    json.dump(dic,f,indent=2)