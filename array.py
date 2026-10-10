import array as arr

array_num=arr.array('i',[1,3,5,3,7,9,3])
print("orignal Array"+str(array_num))

print("number of occurence of number 3 is : "+str(array_num.count(3)))

array_num.reverse()
print(array_num)