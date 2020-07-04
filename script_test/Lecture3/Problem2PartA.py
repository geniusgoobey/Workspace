# Python 3
class Point():
    def __init__(self, x=0, y=0):        
        self.x = x        
        self.y = y
    def __add__(self, other):       
         newX = self.x + other.x        
         newY = self.y + other.y
         return Point(newX, newY)
p = Point(5, 10)

