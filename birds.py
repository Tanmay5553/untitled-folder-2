class parrot :
    species="bird"
    def __init__(self,name,age):

      self.name=name
      self.age=age

ob1=parrot("blu",6)
ob2=parrot("woo",9)

print(ob1.name," is ",ob1.age,"years old")
print(ob2.name," is ",ob2.age,"years old")
