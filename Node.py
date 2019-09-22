import math
from Vec3 import *
from Mesh import *

class Node(object):
    def __init__(self, mesh):
        self.mesh = mesh
        self.children = []
    
    def addChildren(self, node):
        self.children.append(node)