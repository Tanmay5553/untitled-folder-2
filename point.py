class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def str(self):
        return "({0},{1})".format(self.x,self.y)

ob=print(2,3)
print(ob)