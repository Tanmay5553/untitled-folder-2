word=input("enter the word :")
char=input("enter the character :")

i=1
count=0
while i<(len(word)):
    if word[i]==char:
        count=count+1

    i=i+1
print("the number of times the character appears in word is :",count,"char")
        