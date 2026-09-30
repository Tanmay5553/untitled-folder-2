def matchword(word):
    count=0
    list1=[]
    for i in word:
        if len(i)>1 and i[0]==i[-1]:
            count +=1
            list1 .append(i)

    print(list1)
    print(count)
matchword(["aba","dad","maam","rar"])


