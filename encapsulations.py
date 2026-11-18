class  myClass:
    __PrivateVar=20

    def __PrivMeth(self):
        print("private method")

    def hello(self):
        print("private Variable value : ",myClass.__PrivateVar)

ob= myClass()
ob.hello()
        