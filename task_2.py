import json
with open ('task_1.json','r') as f:
        s=json.load(f)

def group_by_year(movies):    
    l=[]
    for i in movies:
        if i['year'] not in l:
            l.append(i['year'])
        l.sort()
    d={}
    for j in range(len(l)):
        d[l[j]]=[]
        for f in range(len(movies)):
            if movies[f]['year']==l[j]:
                d[l[j]].append(movies[f])
    with open('task_2.json','w')as fi:
        json.dump(d,fi,indent=4)

group_by_year(s)

