# from turtle import *
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()


# N=int(input())
# for i in range(N):
#     l=list(map(int,input().split()))
#     if l[0]>l[1] and l[0]<l[2] or l[0]<l[1] and l[0]>l[2]:
#         print(l[0])
#     elif l[1]>l[0] and l[1]<l[2] or l[1]<l[0] and l[1]>l[2]:
#         print(l[1])
#     elif l[2]>l[0] and l[2]<l[1] or l[2]<l[0] and l[2]>l[1]:
#         print(l[2])


# T=int(input())
# for i in range(T):
#     l=list(map(int,input().split()))
#     print(l)
#     x=l[0]-l[1]
#     if x>0:
#         print(x)
#     else:
#         print(0)

# # cook your dish here
# t=int(input())
# a='bcdfghjklmnpqrstvwxyz'
# for i in range(t):
#     c=0
#     n=input()
#     s=input().lower()
#     for j in s:
#         if j in a:
#             c+=1
#     if c<4:
#         print("YES")
#     elif c==4:
#         print("YES")
#      c>4:
#         print("NO")
    
    
# t=int(input())
# for i in range(t):
#     nk=list(map(int,input().split()))
#     n=list(map(int,input().split()))
#     k=nk[1]
#     for j in range(len(n)):
#         if k>=n[j]:
#             print(1,end="")
#             k=k-n[j]
#         else:
#             print(0,end="")
        

t=int(input())
for i in range(t):
    c=0
    n=int(input())
    s=input()
    for j in s:
        if (j=='a' or j=='e' or j=='i' or j=='u' or j=='o'):
            c=0
        else:
            c+=1
            if c>=4:
                break
    if c>=4:
        print("NO")             
    else:
        print("YES")


t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    for j in s:
        if j=='a'or j=='e'or j=='i'or j=='o' or j=='u':
            count=0
        else:
            count+=1
            if count>=4:
                break
    if count>=4:
        print('no')
    else:
        print('yes')