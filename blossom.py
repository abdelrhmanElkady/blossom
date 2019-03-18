from OpenGL.GL import*
from OpenGL.GLUT import*
import numpy as np
from math import *

def drawCircle(r=0.1, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + xc, y + yc)
    glEnd()

def drawHalfCircle(r=0.1, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(pi,2 * pi, 0.001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + xc, y + yc)
    glEnd()


def drawHalfUpCircle(r=0.1, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, pi, 0.001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + xc, y + yc)
    glEnd()


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    # body
    glColor3f(0, 0, 0)
    glLineWidth(4)
    for (R, G, B, type) in ((1, 0.2, 0.3, GL_POLYGON), (0, 0, 0, GL_LINE_STRIP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.1, -0.3)
        glVertex(-0.13, -0.63)
        glVertex(0.13, -0.63)
        glVertex(0.1, -0.3)
        glEnd()
    #dress
    for (R, G, B, type) in ((0, 0, 0, GL_POLYGON), (0, 0, 0, GL_LINE_STRIP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.1, -0.3825)
        glVertex(-0.12, -0.5)
        glVertex(0.12, -0.5)
        glVertex(0.1, -0.3825)
        glEnd()

    #backUpperLegs
    for (R, G, B, type) in ((0, 0, 0, GL_POLYGON), (0, 0, 0, GL_LINE_STRIP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.12, -0.63)
        glVertex(-0.12, -0.9)
        glVertex(0.12, -0.9)
        glVertex(0.12, -0.63)
        glEnd()
    #backDownLegs
    glColor(0, 0, 0)
    drawHalfCircle(0.07, 0.06, -0.9)

    glColor(0, 0, 0)
    drawHalfCircle(0.07, -0.06, -0.9)

    #frontUpperLegs
    for (R, G, B, type) in ((1, 1, 1, GL_POLYGON), (1, 1, 1, GL_LINE_STRIP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(0.095, -0.66)
        glVertex(0.095, -0.85)
        glVertex(0.03, -0.85)
        glVertex(0.03, -0.66)
        glEnd()

    for (R, G, B, type) in ((1, 1, 1, GL_POLYGON), (1, 1, 1, GL_LINE_STRIP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.095, -0.66)
        glVertex(-0.095, -0.85)
        glVertex(-0.03, -0.85)
        glVertex(-0.03, -0.66)
        glEnd()

    #froneDownLegs

    glColor(1, 1, 1)
    drawHalfCircle(0.05, 0.06, -0.88)

    glColor(1, 1, 1)
    drawHalfCircle(0.05, -0.06, -0.88)

    # fyoonka

    glColor(0.9, 0, 0)
    drawHalfUpCircle(0.4, 0, 0.55)

    for (R, G, B, type) in ((1, 1, 1, GL_POLYGON), (1, 1, 1, GL_LINE_STRIP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(0.4, 0.9)
        glVertex(0.35, 0.9)
        glVertex(0, 0)
        glEnd()
    for (R, G, B, type) in ((1, 1, 1, GL_POLYGON), (1, 1, 1, GL_LINE_STRIP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.4, 0.9)
        glVertex(-0.35,  0.9)
        glVertex(0, 0)

        glEnd()












    #head

    glColor3f(0, 0, 0)
    drawCircle(0.52, 0, 0.2)

    glColor3f(.9, .8, .7)
    drawCircle(0.5, 0, 0.2)
    #eyes
    glColor3f(0, 0,0)
    drawCircle(0.24,-0.28 , 0.2)

    glColor3f(0, 0,0)
    drawCircle(0.24,0.28 , 0.2)

    glColor3f(1, 1,1)
    drawCircle(0.23,-0.28 , 0.2)

    glColor3f(1, 1,1)
    drawCircle(0.23,0.28 , 0.2)

    glColor3f(1, 0.2,.3)
    drawCircle(0.2,-0.249 , 0.2)

    glColor3f(1, 0.2,.3)
    drawCircle(0.2,0.249 , 0.2)

    glColor3f(0, 0,0)
    drawCircle(0.145,-0.2 , 0.2)

    glColor3f(0, 0,0)
    drawCircle(0.145,0.2 , 0.2)

    glColor3f(1, 1,1)
    drawCircle(0.07,-0.2 , 0.2)

    glColor3f(1, 1,1)
    drawCircle(0.07,0.2 , 0.2)

    # smile
    glColor(0, 0, 0)
    drawHalfCircle(0.12, 0, -0.09)

    glColor(0.9, 0.8, 0.7)
    drawHalfCircle(0.12, 0, -0.079)

    #hair
    glColor(0, 0, 0)
    drawHalfUpCircle(0.52, 0, 0.22)

    glColor(0.9, 0.5, 0.1)
    drawHalfUpCircle(0.5, 0, 0.22)

    for (R, G, B, type) in ((0.9, 0.8, 0.7, GL_POLYGON), (0.9, .8, .7, GL_LINE_STRIP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(0.029, 0.2)
        glVertex(0, 0.45)
        glVertex(-0.029, 0.2)

        glEnd()

















    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(200, 200)
glutInitWindowSize(500, 500)
glutCreateWindow(b"blossom")
glutDisplayFunc(draw)
glutMainLoop()
