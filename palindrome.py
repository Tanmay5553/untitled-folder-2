def palindrome(t):
    e=len(t)-1
    s=0

    while (s<e):
        if (t[s] != t[e]):
            return False

        s+= 1
        e-= 1
    return True
tuple1=(1,2,3,3,2,4)
if (palindrome(tuple1)):
    print("it is a palindrome")

else:
    print("it is not a palindrome")
            
        