import math
import random
from Vec3 import *
from Mesh import *
from Node import *
from Camera import *
from Scene import *

class Display(object):
    def __init__(self, scene):
        self.scene = scene


    def midpoint(self, poly):
        # p1, p2, p3 = poly
        # x = (p1.x+p2.x+p3.x)/3
        # y = (p1.y+p2.y+p3.y)/3
        # z = (p1.z+p2.z+p3.z)/3
        # return Vec3(x,y,z)
        # l12 = (p2-p1).lengthSQ()
        # l13 = (p3-p1).lengthSQ()
        # l23 = (p3-p2).lengthSQ()
        # sides = [(l12, (p1, p2)), (l13, (p1, p3)), (l23, (p2, p3))]
        # sides.sort()
        # (x, (y, z)) = sides[2]
        # longVector = z-y
        # (x2, (y2, z2)) = sides[1]
        # shortNormal = (z2-y2)-longVector.normalized()*((z2-y2)*longVector/(x**(.05)))
        # return y+longVector*(.5)+shortNormal*(.5)
        
        ##method 3
        maxX, minX = float('-inf'), float('inf')
        maxY, minY = float('-inf'), float('inf')
        maxZ, minZ = float('-inf'), float('inf')
        for v in poly:
            if v.x > maxX:
                maxX = v.x
            if v.x < minX:
                minX = v.x
            if v.y > maxY:
                maxY = v.y
            if v.y < minY:
                minY = v.y
            if v.z > maxZ:
                maxZ = v.z
            if v.z < minZ:
                minZ = v.z
        return Vec3((maxX+minX)/2, (maxY+minY)/2, (maxZ+minZ)/2) 
            
        
    
    
    def distPoly(self, midPoly):
        midpoint, poly = midPoly
        distVector = midpoint - self.scene.camera.position
        distanceSQ = distVector.lengthSQ()
        return (distanceSQ, poly)
    
    def sortedDistance(self, polygonList):
        midpointPolygons = list(map(lambda poly: (self.midpoint(poly), poly), polygonList))
        distancePolygons = list(map(self.distPoly, midpointPolygons))
        distancePolygons.sort()
        #distancePolygons.reverse()
        return distancePolygons
        
    def collect(self, node, polygonList=None):
        if polygonList == None:
            polygonList = []
        polygonList.extend(node.mesh.polygons)
        for i in range(len(node.children)):
            self.collect(node.children[i], polygonList)
        return polygonList
    
    def screenCoordinates(self, coord):
        vecA = coord-self.scene.camera.position
        vecF = self.scene.camera.frameVectors[4]
        # print(vecF.x)
        # print(vecF.y)
        # print(vecF.z)
        # print(vecA.x)
        # print(vecA.y)
        # print(vecA.z)
        s = vecF.lengthSQ()/(vecF*vecA)
        intersectionCoord = self.scene.camera.position+vecA*s
        screenV = intersectionCoord-self.scene.camera.frame[0]
        y = screenV*self.scene.camera.yAxis
        x = screenV*self.scene.camera.xAxis
        #print(x,y)
        return ((x,y), s)
    
    def draw(self, canvas, distPoly):
        distance, polygon = distPoly
        v1, v2, v3 = polygon
        p1, s1 = self.screenCoordinates(v1)
        p2, s2 = self.screenCoordinates(v2)
        p3, s3 = self.screenCoordinates(v3)
        if s1 < 0 and s2 < 0 and s3 < 0:
            canvas.create_polygon(p1, p2, p3, outline="black", fill="white")

        
    
    def drawAll(self, canvas):
        polygonList = self.collect(self.scene.root)
        sortedPolygonList = self.sortedDistance(polygonList)
        # print(sortedPolygonList)
        for i in range(len(sortedPolygonList)-1, -1, -1):
            self.draw(canvas, sortedPolygonList[i])
        
        # for distPoly in sortedPolygonList:
        #     self.draw(canvas, distPoly)
             
        


    
    