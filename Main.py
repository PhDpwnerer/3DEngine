import math
import random
from Vec3 import *
from Mesh import *
from Node import *
from Camera import *
from Scene import *
from Display import *


#### Graphics Functions ####

from tkinter import *

def init(data):
    data.level = Scene(Node(Mesh.triangularPyramid(Vec3(0,0,500))), Camera(Vec3(0,0,0), 250, data.width, data.height))
    data.level.root.addChildren(Node(Mesh.cube(Vec3(200,200,500))))
    data.screen = Display(data.level)
    data.paused = True
    data.looking = False
    data.prevX = 0
    data.prevY = 0

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if event.keysym == "k":
        data.paused = not(data.paused)
    if event.keysym == "w":
        data.screen.scene.camera.move(0,0,10)
    if event.keysym == "a":
        data.screen.scene.camera.move(-10,0,0)
    if event.keysym == "s":
        data.screen.scene.camera.move(0,0,-10)
    if event.keysym == "d":
        data.screen.scene.camera.move(10,0,0)
    if event.keysym == "q":
        data.screen.scene.camera.move(0,-10,0)
    if event.keysym == "e":
        data.screen.scene.camera.move(0,10,0)
    if event.keysym == "Up":
        data.screen.scene.camera.rotateYZ(5)
    if event.keysym == "Down":
        data.screen.scene.camera.rotateYZ(-5)
    if event.keysym == "Left":
        data.screen.scene.camera.rotateXZ(5)
    if event.keysym == "Right":
        data.screen.scene.camera.rotateXZ(-5)
    
def mouseMotionR(event, data):
    if data.looking == False:
        data.looking = True
        data.prevX = event.x
        data.prevY = event.y
        deltaX = 0
        deltaY = 0
    else:
        deltaX = event.x-data.prevX
        deltaY = event.y-data.prevY
    angleXZ = math.degrees(math.atan(0.5*deltaX/data.screen.scene.camera.focalLength))
    angleYZ = math.degrees(math.atan(0.5*deltaY/data.screen.scene.camera.focalLength))
    data.screen.scene.camera.rotateXZ(angleXZ)
    data.screen.scene.camera.rotateYZ(angleYZ)
    data.prevY = event.y
    data.prevX = event.x

def mouseReleaseR(event, data):
    data.looking = False

def timerFired(data):
    pass
    if not(data.paused):
        data.screen.scene.root.mesh.rotateXZ(5)
        data.screen.scene.root.mesh.rotateXY(-5)
        data.screen.scene.root.mesh.rotateYZ(-5)
        data.screen.scene.root.children[0].mesh.rotateXZ(5)
        data.screen.scene.root.children[0].mesh.rotateXY(-5)
        data.screen.scene.root.children[0].mesh.rotateYZ(-5)
        

def redrawAll(canvas, data):
    data.screen.drawAll(canvas)

#################################################################
# use the run function as-is
#################################################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='black', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)
        
    def mouseMotionRWrapper(event, canvas, data):
        mouseMotionR(event, data)
        redrawAllWrapper(canvas, data)
    
    def mouseReleaseRWrapper(event, canvas, data):
        mouseReleaseR(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<B3-Motion>", lambda event:
                            mouseMotionRWrapper(event, canvas, data))
    root.bind("<ButtonRelease-3>", lambda event: 
                            mouseReleaseRWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(600, 600)