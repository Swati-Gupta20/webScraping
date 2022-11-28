import json

with open('task_5.json','r')as f:
    s=json.load(f)

l=[]
for i in s:
    if i['language'] not in l:
        l.append(i['language'])
dic={}
for j in l:
    c=0
    for k in s:
        if k['language']==j:
            c+=1
    dic[j]=c
with open('task_6.json','w')as f:
    json.dump(dic,f,indent=2)
