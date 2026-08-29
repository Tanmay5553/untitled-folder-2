def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

print ("factorial of 0:",factorial(0))
print ("factorial of 1:",factorial(1))
print("factorial of 2:" ,factorial(2))
print("factorial of 3:" ,factorial(3)) 
print("factorial of 4:" ,factorial(4))
print("factorial of 5:" ,factorial(5))