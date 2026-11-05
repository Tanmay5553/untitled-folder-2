class bird:
    def __init__(self):
        print("bird constructor")

    def Accommodation(self):
        print("birds live in nest")

    def Act(self):
        print("birds can fly")

class penguin(bird):
    def __init__(self):
        print("penguin constructor")

    def Accommodation(self):
        print("penguin lives in coastal areas ")

    def Act(self):
        print("penguins can walk")

ob=penguin()
ob.Accommodation()
ob.Act()