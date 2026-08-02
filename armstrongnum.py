num=int(input("enter the number :"))

sum=0
temp=num

while temp>0:

     digit = temp%10
     sum+=digit**3
     temp//=10

if sum==num:
     print("the number is armstrong number")
else:
     print("the numbeer is not a armstrong number")