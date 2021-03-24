#HOMEWORK - Write a class for an Airplane

class Car:
    
    
    #Constructor Method
    #"sedan" "coupe" "truck"
    
    maxSpeed = 70
    fuelTankSize = 25
    carIsOn = False
    
    def slowDown(self):
        print("Screeeeech")
        
    def turn(self,direction):
        print("We are turning " + direction)
    
    def checkGas(self):
        return self.fuel
        
    def refuel(self,howMuchGas):
        if self.fuel + howMuchGas > self.fuelTankSize:
            return False
        else:
            self.fuel += howMuchGas
            return True
    
    
    def __init__(self,paintColor,model,hasHeater,hasRadio,wheelSize,fuelInput):
        self.color = paintColor
        self.type = model
        self.heater = hasHeater
        self.radio = hasRadio
        self.wheels = wheelSize
        self.fuel = fuelInput
        
        
    def start(self):
        self.carIsOn = True
    
    
    def drive(self):
        if self.carIsOn == False:
            print("The car is not on yet")
        else:
            self.fuel -= 1
            print("Cruising Down The Road!")
        
    def speedUp(self):
        print("Zoom Zoom")
        
    
        
       
TheosCar = Car("green","Cybertruck",True,True,28,15)
RussCar = Car("red","limo",False,True,18,10)

TheosCar.drive()
TheosCar.drive()
TheosCar.drive()
TheosCar.start()
TheosCar.drive()
TheosCar.drive()
TheosCar.turn("left")
TheosCar.turn("right")

print(  TheosCar.refuel(99) )
