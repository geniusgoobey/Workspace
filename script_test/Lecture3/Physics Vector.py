class Vector2D(object):
    '''Vector2D object with an x and y value.'''
    def __init__(self, x=0, y=0):
        self.X = float(x)
        self.Y = float(y)
        
    def __add__(self, other):
        if isinstance(other, Vector2D):
            newX = self.X + other.X
            newY = self.Y + other.Y
            return Vector2D(newX, newY)
        else:
            raise ValueError("Can only add a vector to another vector.")
            
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            newX = self.X - other.X
            newY = self.Y - other.Y
            return Vector2D(newX, newY)
        else:
            raise ValueError("Can only subtract a vector to another vector.")
            
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            newX = self.X * scalar
            newY = self.Y * scalar
            return Vector2D(newX, newY)
        else:
            raise ValueError("Can only multiply a vector to a scalar.")
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            newX = self.X / scalar
            newY = self.Y / scalar
            return Vector2D(newX, newY)
        else:
            raise ValueError("Can only divide a vector to a scalar.")
            
    def __str__(self):
        return "(X = {}, Y = {})".format(self.X, self.Y)
        
        
v1 = Vector2D(2, 3)
v2 = Vector2D(7, 2)

print("Vector 1: {}".format(v1))
print("Vector 2: {}".format(v2))
print("V1 + V2 = {}".format(v1 + v2))
print("V1 - V2 = {}".format(v1 - v2))
print("V1 * 3.14 = {}".format(v1 * 3.14))
print("V2 / 2 = {}".format(v2 / 2))
print("Vector 1: {}".format(v1))
print("Vector 2: {}".format(v2))