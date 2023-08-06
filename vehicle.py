#create a class car which has its attributes as name, model and speed.
#Create a function display to display all the car details.
#Create a method accelerate to increase the speed of the car by 5 everytime the method is invoked.
#Create a method brake to reduce the speed of the car by 10 every time its invoked.
#take initial speed as 60mph apply accelerate and brake method multiple times to stop the car.
class Car:
    def __init__(self,name,model,speed):
        self.name=name
        self.model=model
        self.speed=speed
    def display(self):
        print(self.name,self.model,self.speed)
    def accelerate(self,default):
        self.speed=self.speed+default
    def brake(self,default1):
        self.speed=self.speed-default1
mercedes=Car('Merceded Benz','EQS',190)
BMW=Car('BMW','5 series',200)
Hyundai=Car('Hyundai','I10',140)
mercedes.accelerate(5)
mercedes.brake(10)
BMW.accelerate(5)
BMW.brake(10)
Hyundai.accelerate(5)
Hyundai.brake(10)
print(mercedes.speed)
print(BMW.speed)
print(Hyundai.speed)






