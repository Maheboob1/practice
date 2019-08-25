a=[3,2,1,6,5,4,9,8,7]
b=[]
for i in a:
    if i not in b:
        if i%2==0:
            b.append(i)
print((sorted(b)))

