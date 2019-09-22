import math
from Vec3 import *

class Mesh(object):
    def __init__(self, position, vertexVectors, faces):
        self.position = position
        self.vertexVectors = vertexVectors
        self.vertices = [Vec3(0,0,0)]*len(self.vertexVectors)
        self.faces = faces #represents the indices from self.vertices
        #polygons represent the actual vertices
        self.polygons = [(Vec3(0,0,0),Vec3(0,0,0),Vec3(0,0,0))]*len(self.faces)
        self.update()
    
    def scale(self, x, y, z):
        for i in range(len(self.vertexVectors)):
            self.vertexVectors[i] = self.vertexVectors[i].scale(x, y, z)
        self.update()
        
    def rotateXY(self, angle):
        for i in range(len(self.vertexVectors)):
            self.vertexVectors[i] = self.vertexVectors[i].rotateXY(angle)
        self.update()
    
    def rotateXZ(self, angle):
        for i in range(len(self.vertexVectors)):
            self.vertexVectors[i] = self.vertexVectors[i].rotateXZ(angle)
        self.update()
        
    def rotateYZ(self, angle):
        for i in range(len(self.vertexVectors)):
            self.vertexVectors[i] = self.vertexVectors[i].rotateYZ(angle)
        self.update()
        
    def move(self, x, y, z):
        self.position = self.position + Vec3(x, y, z)
        self.update()
                
    #for map function
    def getFaceVertices(self, face):
        x,y,z = face
        return (self.vertices[x], self.vertices[y], self.vertices[z])
    
    def update(self):
        for i in range(len(self.vertices)):
            self.vertices[i] = self.position+self.vertexVectors[i]
        self.polygons = list(map(self.getFaceVertices, self.faces))
            
        
    @staticmethod
    def cube(position):
        vertexVectors = [Vec3(-100, 100, -100), Vec3(100, 100, -100), 
                         Vec3(100, -100, -100), Vec3(-100, -100, -100),
                         Vec3(-100, 100, 100), Vec3(100, 100, 100),
                         Vec3(100, -100, 100), Vec3(-100, -100, 100)]
        #alternate = list(map(lambda x: x.scale(0.6, 0.6, 0.6), vertexVectors))
        # faces = [(0,1,2), (0,2,3), (0,1,4), (1,4,5), (1,2,6), (1,5,6),
        #          (4,5,7), (5,6,7), (2,3,6), (3,6,7), (0,3,4), (3,4,7)]
        faces = [(0,1,2), (0,2,3), (0,4,5), (0,1,5), (0,3,4), (3,4,7),
                 (1,2,5), (2,5,6), (2,3,6), (3,6,7), (4,5,6), (4,6,7)]
                 
        return Mesh(position, vertexVectors, faces)
        
    def triangularPyramid(position):
        vertexVectors = [Vec3(0,0,47.87), Vec3(28.867,0,0), 
                         Vec3(-14.434,25,0), Vec3(-14.434,-25,0)]
        vertexVectors = list(map(lambda vector: vector.scale(3,3,3), vertexVectors))
        faces = [(0,1,2), (0,2,3), (0,1,3), (1,2,3)]
        return Mesh(position, vertexVectors, faces)
        