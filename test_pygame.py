
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


import sys


# Global values
SCREEN_SIZE = (640, 480)


# === Initioal Processing ===
def init():
	pygame.init()


# === draw object ===
class Cube(object):
	"""docstring for ViewCube"""
	def __init__(self, color):
		self.color = color
		self.verticies = (
						( 1, -1, -1),
						( 1,  1, -1),
						(-1,  1, -1),
						(-1, -1, -1),
						( 1, -1,  1),
						( 1,  1,  1),
						(-1, -1,  1),
						(-1,  1,  1)
						)
		self.edges = (
					(0,1),
					(0,3),
					(0,4),
					(2,1),
					(2,3),
					(2,7),
					(6,3),
					(6,4),
					(6,7),
					(5,1),
					(5,4),
					(5,7)
					)
	
	def viewObject(self):
		glBegin(GL_LINES)
		for edge in self.edges:
			for vertex in edge:
				glColor3fv(self.color)
				glVertex3fv(self.verticies[vertex])
		glEnd()

class Lamp(object):
	"""docstring for Lamp"""
	def __init__(self, name):
		self.name = name

	def viewObject(self):
		pass
		



# === MAIN ===
def main():
	# init
	init()
	pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF | OPENGL)	# view window
	pygame.display.set_caption(u"test")	# window title

	# decide camera and objects position
	gluPerspective(45, (SCREEN_SIZE[0]/SCREEN_SIZE[1]), 0.1, 50.0)	# y, aspect, near, far
	glTranslatef(0.0, 0.0, -5)	# translate (x,y,z)

	# declaration
	obj = Cube([1.0,0.0,0.0])	# (color)


	# loop
	while True:
		# rotate coordinate
		glRotatef(0.1, 0, 1, 0)	# angle, vx,vy,vz <- Axis of rotation
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		# draw objects
		obj.viewObject()

		# view screen
		pygame.display.flip()


		# invent processing
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
		pygame.time.wait(10)


if __name__ == "__main__":
	main()


