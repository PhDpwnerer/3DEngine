import math
from Vec3 import *

class Camera(object):
    def __init__(self, position, focalLength, w, h):
        self.position = position
        #storing focalLength info in case want to add feature of changing focal length
        self.focalLength = focalLength
        self.width = w
        self.height = h
        ### review the signs when testing (these are for the coordinates of the four corners of the screen, z-axis coming our way)
        self.topLeft = Vec3((-1)*self.width/2, self.height/2, (-1)*focalLength)
        self.topRight = Vec3(self.width/2, self.height/2, (-1)*focalLength)
        self.bottomRight = Vec3(self.width/2, (-1)*self.height/2, (-1)*focalLength)
        self.bottomLeft = Vec3((-1)*self.width/2, (-1)*self.height/2, (-1)*focalLength)
        self.center = Vec3(0, 0, (-1)*focalLength)
        self.frameVectors = [self.topLeft, self.topRight, self.bottomRight, self.bottomLeft, self.center]
        self.frame = [Vec3(0,0,0),Vec3(0,0,0),Vec3(0,0,0),Vec3(0,0,0),Vec3(0,0,0)]
        
        self.yAxis = Vec3(0,0,0)
        self.xAxis = (Vec3(0,0,0)) 
        self.update()
        
    def rotateXY(self, angle):
        for i in range(len(self.frameVectors)):
            self.frameVectors[i] = self.frameVectors[i].rotateXY(angle)
        self.update()
    
    def rotateXZ(self, angle):
        for i in range(len(self.frameVectors)):
            self.frameVectors[i] = self.frameVectors[i].rotateXZ(angle)
        self.update()
            
    def rotateYZ(self, angle):
        for i in range(len(self.frameVectors)):
            self.frameVectors[i] = self.frameVectors[i].rotateYZ(angle)
        self.update()
            
    #EW = East-West, UD = Up-Down, NS = North-South
    def move(self, EW, UD, NS):
        horizontal = self.xAxis.normalized() * EW * (-1)
        vertical = self.yAxis.normalized() * UD
        forward = self.frameVectors[4].normalized() * NS * (-1)
        
        self.position = self.position + forward + horizontal + vertical
        self.update()
        
    def update(self):
        for i in range(len(self.frame)):
            self.frame[i] = self.position+self.frameVectors[i]
        self.yAxis = (self.frame[3]-self.frame[0]).normalized()
        self.xAxis = (self.frame[1]-self.frame[0]).normalized()