f=open("sample1.txt","r")
a=(f.read())

print(a)
L1=[i for i in a if i.isdigit()]
print(L1)
L2=[i for i in a if i.isalpha()]
print(L2)
b=L1+L2

L3=[i for i in a if i not in b]
print(L3)