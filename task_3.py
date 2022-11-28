import json

with open ('task_1.json','r') as f:
        s=json.load(f)

def group_by_decade(movies):
    l=[]
    for i in movies:
        if i['year'] not in l:
            l.append(i['year'])
    l.sort()
    l2=[]
    for x in l:
        a=x%10
        if x-a not in l2:
            l2.append(x-a)
    d={}
    for j in range(len(l2)):
        d[l2[j]]=[]
        for f in range(len(movies)):
            if movies[f]['year']>=l2[j] and movies[f]['year']<=(l2[j]+9) :
                d[l2[j]].append(movies[f])
    with open('task_3.json','w')as fi:
        json.dump(d,fi,indent=4)

group_by_decade(s)