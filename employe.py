class person :
    def __init__(self,name,idNumber):
        self.name=name
        self.idNumber=idNumber
    def display(self):
        print("name= ",self.name)
        print("idNumber= ",self.idNumber)

class employe(person):
    def __init__(self, name, idNumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name, idNumber)
ob=employe("Tanmay",10094,200000,"developer")
ob.display()