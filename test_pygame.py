
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
verticies = (
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1)
	)

edges = (
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


def Cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(verticies[vertex])
	glEnd()




# === MAIN ===
def main():
	# init
	init()
	pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF | OPENGL)	# view window
	pygame.display.set_caption(u"test")	# window title

	# decide camera and objects position
	gluPerspective(45, (SCREEN_SIZE[0]/SCREEN_SIZE[1]), 0.1, 50.0)	# y, aspect, near, far
	glTranslatef(0.0, 0.0, -5)	# translate (x,y,z)

	# loop
	while True:
		# rotate coordinate
		glRotatef(0.1, 0, 1, 0)	# angle, vx,vy,vz <- Axis of rotation
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		# draw objects
		Cube()

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


