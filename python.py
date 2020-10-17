n=int(input("enter size of array"))
a=[]
for i in range(n):
    a.append(int(input("enter number12")))
print(a)
b=set(a)
d=0
for i in b:
    c=a.count(i)
    if c%2==0:
        d+=c
    elif c==1:
        d+=0
    else:
        d+=c-1

print(d//2)