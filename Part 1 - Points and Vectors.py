import math

### Point and Vector classes ###

class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def draw(self):
        print("(", self.x,",", self.y,",", self.z,")")
    
    def addVectorToPoint(self, v):
        self.x += v.x
        self.y += v.y
        self.z += v.z
    
    def substractVectorFromPoint(self, v):
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z
    
    def substractPointFromPoint(self, point):
        vX = self.x - point.x
        vY = self.y - point.y
        vZ = self.z - point.z
        return Vector(vX, vY, vZ)
        
class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def draw(self):
        print("(", self.x,",", self.y,",", self.z,")")
    
    def addVectorToVector(self, v):
        vX = self.x + v.x
        vY = self.y + v.y
        vZ = self.z + v.z
        return Vector(vX, vY, vZ)
        
    def substractVectorFromVector(self, v):
        vX = self.x - v.x
        vY = self.y - v.y
        vZ = self.z - v.z
        return Vector(vX, vY, vZ)
    
    #angle arguments are in degrees, not radians
    def rotateXY(self, angle):
        x = self.x*math.cos(math.radians(angle)) - self.y*math.sin(math.radians(angle))
        y = self.x*math.sin(math.radians(angle)) + self.y*math.cos(math.radians(angle))
        self.x = x
        self.y = y
                
    def rotateXZ(self, angle):
        x = self.x*math.cos(math.radians(angle)) + self.z*math.sin(math.radians(angle))
        z = -self.x*math.sin(math.radians(angle)) + self.z*math.cos(math.radians(angle))
        self.x = x
        self.z = z
        
    def rotateYZ(self, angle):
        y = self.y*math.cos(math.radians(angle)) - self.z*math.sin(math.radians(angle))
        z = self.y*math.sin(math.radians(angle)) + self.z*math.cos(math.radians(angle))
        self.x = x
        self.y = y
        
    #scaling
    def scale(self, x, y, z)
        self.x *= x
        self.y *= y
        self.z *= z

p1 = Point(1,2,1)
p2 = Point(0,4,4)
v1 = Vector(2,0,0)
p1.draw()
p2.draw()
v2 = p1.substractPointFromPoint(p2)
v1 = v1.addVectorToVector(v2)
p1.addVectorToPoint(v1)
p1.draw()
p2.substractVectorFromPoint(v2)
p2.draw()

v3 = Vector(3,4,5)
v3.rotateXY(90)
v3.draw()
    