class Employe:
    def __init__(self):
        print("constructor called !")

    def __del__(self):
        print("destructor called !")

def createobj():
        print("making obj !!...")
        ob=Employe()
        print("obj created")
        return ob

createobj()
    
