import math
from Vec3 import *
from Mesh import *
from Node import *
from Camera import *

class Scene(object):
    def __init__(self, node, camera):
        self.root = node
        self.camera = camera