
#coding:utf-8
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


# === Global Value ===
WIDTH = 300
HEIGHT = 300

angle = 0.0


# === INIT ===
def init(width, height):
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glEnable(GL_DEPTH_TEST)  # 隠面消去を有効に

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)  # 投影変換



# === View Screen ===
def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	# 視野変換：カメラの位置と方向のセット
	gluLookAt(5.0,4.0,1.0, 0.0,0.0,0.0, 0.0,0.0,1.0)	# camera coordinates, camera angle, camera top
	
	# draw objects
	glRotatef(angle, 0.0, 0.0, 1.0)	# rotation
	glColor3f(1.0, 0.0, 0.0)	# (rad, green, blue)   0.0~1.0
	glutWireSphere(1.0, 30, 30)	# (radius, partitions of mdridian, parallel)

	glFlush()  # OpenGLコマンドの強制実行



# === Resize ===
def reshape(width, height):
	"""画面サイズの変更時に呼び出されるコールバック関数"""
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)


# === IDLE ===
def idle():
	"""アイドル時に呼ばれるコールバック関数"""
	global angle
	angle += 0.05
	glutPostRedisplay()	# redisplay



# === MAIN ===
def main():
	# initial processing
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
	glutInitWindowSize(WIDTH, HEIGHT)	# ウィンドウサイズ
	glutInitWindowPosition(100, 100)	# ウィンドウ位置
	glutCreateWindow(u"Test")	# ウィンドウを表示
	glutDisplayFunc(display)	# 描画コールバック関数を登録
	glutReshapeFunc(reshape)	# リサイズコールバック関数の登録
	glutIdleFunc(idle)			# アイドルコールバック関数を登録

	init(WIDTH, HEIGHT)

	# loop
	glutMainLoop()


if __name__ == "__main__":
	main()