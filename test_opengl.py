#! /usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


"""
# === Initial Processing ===
def init():
	glClearColor(0.0, 0.0, 1.0, 1.0)

	# setting of coordinate system\
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


# === Display Processing ===
def display():
	glClear(GL_COLOR_BUFFER_BIT)

	glColor3f(1.0, 0.0, 0.0)
	glBegin(GL_QUADS)
	glVertex2f(-0.5, -0.5)
	glVertex2f(-0.5,  0.5)
	glVertex2f( 0.5,  0.5)
	glVertex2f( 0.5, -0.5)
	glEnd()

	glFlush()


# === MAIN ===
def main():
	# init
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
	glutInitWindowSize(300, 300)
	glutInitWindowPosition(100, 100)
	glutCreateWindow("")
	glutDisplayFunc(display)
	init()

	# loop
	glutMainLoop()


if __name__ == "__main__":
	main()
"""

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(300, 300)  # ウィンドウサイズ
    glutInitWindowPosition(100, 100)  # ウィンドウ位置
    glutCreateWindow("OpenGLウィンドウの表示")  # ウィンドウを表示
    glutDisplayFunc(display)  # 描画関数を登録
    init()
    glutMainLoop()

def init():
    glClearColor(0.0, 0.0, 1.0, 1.0)  # クリア色の指定

def display():
    """描画処理"""
    glClear(GL_COLOR_BUFFER_BIT)  # 画面のクリア
    glFlush()  # OpenGLコマンドの強制実行

if __name__ == "__main__":
    main()