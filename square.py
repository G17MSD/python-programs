#write a program to create a class rectangle and find its parameter and area using 2 different functions.
class Rectangle:
    def __init__(self,length,base):
        self.length=length
        self.base=base
    def perimeter(self):
        return self.length*2+self.base*2
    def area(self):
        return self.length*self.base
object=Rectangle(32,12)
print(object.perimeter())
print(object.area())

#create a class square and find area and perimeter
class Square:
    def __init__(self,length):
        self.length=length
    def perimeter(self):
        return self.length*4
    def area(self):
        return self.length*self.length
object=Square(80)
print(object.perimeter())
print(object.area())


class Shape:
    def __init__(self, length) -> None:
        self.length = length
# Square (child class) is inheriting from the Shape (Parent class)
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self, length)
    def perimeter(self):
        return self.length*4
    def area(self):
        return self.length*self.length


class Shape:
    def __init__(self, length) -> None:
        self.length = length
# Square (child class) is inheriting from the Shape (Parent class)
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self, length)
    def perimeter(self):
        return self.length*4
    def area(self):
        return self.length*self.length

# Rectangle (child class) is inheriting from the Shape (Parent class)
class Rectangle(Shape):
    def __init__(self, length, base):
        Shape.__init__(self, length)
        self.base=base
    def perimeter(self):
        return self.length*2+self.base*2
    def area(self):
        return self.length*self.base

# objects
s=Square(80)
r=Rectangle(32,12)

print(s.perimeter())
print(s.area())

print(r.perimeter())
print(r.area())

