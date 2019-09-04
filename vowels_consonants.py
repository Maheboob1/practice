
a=input(str("Enter a string: "))
vowel=0
consonants=0


for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" :
        vowel +=1
        #print(list(i),vowel)

    else:
        consonants +=1
        #print(list(i),consonants)


print(list(set(i)),vowel)
print(list(i),consonants)