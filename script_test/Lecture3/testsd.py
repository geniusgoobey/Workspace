from math import sqrt

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.X, self.Y, self.Z = x, y, z
        self.mag = self.__mag()
    
    def __mag(self):
        return sqrt(self.X ** 2 + self.Y ** 2 + self.Z ** 2)
    
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
            return Vector3()
        return Vector3(
            self.X / self.mag, self.Y / self.mag, self.Z / self.mag
        )

if __name__ == "__main__":
    v0 = Vector3()
    v1 = Vector3(3, 2, 1.5)
    v2 = Vector3(4, 7, 10) 

    print(v0.mag)
    print(v0.normalized())
    print(f"v1.mag = {v1.mag}")
    print(f"v2.mag = {v2.mag}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3.2 = {v1 * 3.2}")
    print(f"v2 * 2 = {v2 * 2}")
    print(f"v1 normalized = {v1.normalized()}")
    print(f"v2 normalized = {v2.normalized()}")