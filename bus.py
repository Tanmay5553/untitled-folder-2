class vehical:
    def __init__(self,name,maxSpeed,mileage):
        self.name=name
        self.maxSpeed=maxSpeed
        self.mileage=mileage

class bus(vehical):
    pass
ob=bus("school bus",200,45)

print("bus name = ",ob.name)
print("maxSpeed = ",ob.maxSpeed)
print("mileage = ",ob.mileage)
