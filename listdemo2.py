list_1=[10,20,5,30,4]
print(list_1)

sum=0
for i in list_1:
    sum=sum+i

avg=sum/len(list_1)
print(avg)
list_1.sort()
print("smallest vaalue is ",list_1[0])
print("greatest value is",list_1[-1])