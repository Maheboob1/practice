f=open("sample.txt","a")
f=open("sample.txt","w")
a="i am a python engineer, python is an interpreter language, python is runtime programming language"
f.write(a)
f=open("sample.txt","r")
print(f.read())
print(a.count("python"))