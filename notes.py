amt=int(input("enter amount"))
note100=amt//100
note50=(amt%100)//50
note10=(amt%100)%50//10

print("notes of 100:",note100)
print("notes of 50:",note50)
print("notes of 10:",note10)