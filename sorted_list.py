a=[3,2,1,6,5,4,9,8,7]
b=[]
c=[]
d=[]
d=a
for i in a:
    if i not in b:
        if i%2==0:
            b.append(i)
        else:
            c.append(i)

print((sorted(b)))
print(sorted(c))
print(sorted(d))
