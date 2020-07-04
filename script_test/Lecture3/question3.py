from math import sqrt

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.X = x
        self.Y = y
        self.Z = z
        self.mag = self.__mag()
    
    def __mag(self):
        x = self.X ** 2.0 
        y = self.Y ** 2.0
        z = self.Z ** 2.0

        return "(" + str(x) + "," + str(y) + "," + str(z) + ")"
    
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError(f"Cannot perform multiplication.  {other} is not a scalar or complex.")
        new_x = self.X * other 
        new_y = self.Y * other 
        new_z = self.Z * other
        return Vector3(new_x, new_y, new_z)

    def __sub__(self, other):
        if not isinstance(other, Vector3):
            raise ValueError(f"Cannot perform subtraction.  {other} is not of type Vector3.")
        new_x = self.X - other.X 
        new_y = self.Y - other.Y 
        new_z = self.Z - other.Z 
        return Vector3(new_x, new_y, new_z)

    def __add__(self, other):
        if not isinstance(other, Vector3):
            raise ValueError(f"Cannot perform addition.  {other} is not of type Vector3.")
        new_x = self.X + other.X 
        new_y = self.Y + other.Y 
        new_z = self.Z + other.Z 
        return Vector3(new_x, new_y, new_z)
    
    def normalized(self):
        if self.mag == 0.0:
           return Vector3(self)
        return Vector3(
            self.X / self.mag, self.Y / self.mag, self.Z / self.mag
        )

if __name__ == "__main__":
    v0 = Vector3()
    v1 = Vector3(3, 2, 1.5)
    v2 = Vector3(4, 7, 10) 

    print(v0.mag)
    print(v0.normalized())

