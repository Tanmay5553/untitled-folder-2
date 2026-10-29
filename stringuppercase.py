class IOString:
    def __init__(self):
        self.str1=""

    def get_string(self):
        self.str1=input("enter the string : ")

    def upper_string(self):
        print("string in upper case : ",self.str1.upper())

ob=IOString()
ob.get_string()
ob.upper_string()

     