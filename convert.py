decimal ="int",(input("Enter a decimal number: "))


binary=""

while decimal > 0:
 
    remainder=decimal%2
    binary="str",(remainder)+binary
    decimal//=2

print(" binary :", binary)