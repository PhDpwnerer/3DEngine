import math

class Vec3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return str((self.x, self.y, self.z))
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __lt__(self, other):
        return self.x<other.x
    
    def __add__(self, other):
        return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)
        
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        
    #scalar multiplication
    def __mul__(self, other):
        if type(other) is Vec3:
            return self.x*other.x+self.y*other.y+self.z*other.z
        else:
            return Vec3(self.x*other, self.y*other, self.z*other)
    
    def lengthSQ(self):
        return self.x**2+self.y**2+self.z**2
        
    def length(self):
        return pow(self.lengthSQ(), 0.5)
    
    def normalized(self):
        return self*(1/self.length())
    
    def scale(self, x, y, z):
        return Vec3(self.x*x, self.y*y, self.z*z)
        
    #angle arguments are in degrees, not radians
    def rotateXY(self, angle):
        x = self.x*math.cos(math.radians(angle)) - self.y*math.sin(math.radians(angle))
        y = self.x*math.sin(math.radians(angle)) + self.y*math.cos(math.radians(angle))
        return Vec3(x, y, self.z)
                
    def rotateXZ(self, angle):
        x = self.x*math.cos(math.radians(angle)) + self.z*math.sin(math.radians(angle))
        z = -self.x*math.sin(math.radians(angle)) + self.z*math.cos(math.radians(angle))
        return Vec3(x, self.y, z)
        
    def rotateYZ(self, angle):
        y = self.y*math.cos(math.radians(angle)) - self.z*math.sin(math.radians(angle))
        z = self.y*math.sin(math.radians(angle)) + self.z*math.cos(math.radians(angle))
        return Vec3(self.x, y, z)


