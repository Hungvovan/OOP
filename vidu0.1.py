def tansuat(n):
    dic={}
    for i in n:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
n=input().split()
a=tansuat(n)
print(a)

for x,y in a.items():
    print(x,":",y)

def nhapdic():
    dic={}
    while True:
        key=input()
        if key=="":
            break
        value=int(input())
        dic[key]=value
    return dic
a=nhapdic()
maxkey=max(a,key=a.get)
lonvalue=a[maxkey]

print(maxkey,":",lonvalue)