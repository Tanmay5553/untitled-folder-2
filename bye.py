valid=True

try:
    n=int(input("Enter a number: "))
    while n%2== 0:
      print("bye,bye")
except ValueError:
    print("handled the exception")