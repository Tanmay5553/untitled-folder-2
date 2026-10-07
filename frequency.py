test = {"car":2,"bike":4,"bicycle":1,"toys":4}
print("orignal : ",str(test))
k=4
res=0
for key in test:
    if test[key]==k:
        res= res+1
print(res)
