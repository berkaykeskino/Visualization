import pygame
import numpy as np
import math

def rotateZ(x, y, z, theta):
    theta = math.radians(theta)
    rotationMatrix = np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0              , 0               , 1]
    ])

    vector = np.array([x,y,z])
    return rotationMatrix.dot(vector)

def rotateX(x, y, z, theta):
    theta = math.radians(theta)
    rotationMatrix = np.array([
        [1              , 0               , 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta), math.cos(theta),],
    ])

    vector = np.array([x,y,z])
    return rotationMatrix.dot(vector)

def rotateY(x, y, z, theta):
    theta = math.radians(theta)
    rotationMatrix = np.array([
        [math.cos(theta), 0, math.sin(theta)],
        [0              , 1               , 0],
        [-math.sin(theta),0, math.cos(theta),],
    ])

    vector = np.array([x,y,z])
    return rotationMatrix.dot(vector)


screenX = 800
screenY = 800

screen=pygame.display.set_mode((screenX,screenY))

play = True

def displayVector(x, y, z):
    center = [screenX / 2, screenY / 2]
    
    pygame.draw.line(screen, (10,10,10),center,[ center[0] + x, center[1] + y ])





plane = [
    [100, 50, 0],
    [100, -50, 0],
    [0, 50, 0],
    [0, -50, 0],
    [-100, 50, 0],
    [-100, -50, 0]
]

cube = [
    [100, 100, 100],
    [100, 100, -100],
    [100, -100, 100],
    [100, -100, -100],

    [-100, 100, 100],
    [-100, 100, -100],
    [-100, -100, 100],
    [-100, -100, -100],
]

#initialrotation
for i in range(len(cube)):
    myvector = cube[i]
    cube[i] = rotateX(myvector[0], myvector[1], myvector[2], 10)
    myvector = cube[i]
    cube[i] = rotateY(myvector[0], myvector[1], myvector[2], 30)

while play:
    #SCREEN COLOUR
    screen.fill((20,120,10))


    #INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play=False

    #2d
    #for i in range(len(plane)):
        #myvector = plane[i]
        #plane[i] = rotateZ(myvector[0], myvector[1], myvector[2], 3)
        #myvector = plane[i]
        #plane[i] = rotateX(myvector[0], myvector[1], myvector[2], 3)
        #myvector = plane[i]
        #plane[i] = rotateY(myvector[0], myvector[1], myvector[2], 3)
        #displayVector(myvector[0],myvector[1],myvector[2])
    
    #3d
    for i in range(len(cube)):
        #myvector = cube[i]
        #cube[i] = rotateZ(myvector[0], myvector[1], myvector[2], 3)
        #myvector = cube[i]
        #cube[i] = rotateX(myvector[0], myvector[1], myvector[2], 3)
        myvector = cube[i]
        cube[i] = rotateY(myvector[0], myvector[1], myvector[2], 3)
        
        displayVector(myvector[0],myvector[1],myvector[2])


    pygame.time.wait(100)
    pygame.display.update()