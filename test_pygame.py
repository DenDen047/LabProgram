
# -*- coding: utf-8 -*-

import pygame
from pygame.local import *
import sys


# Global values
SCREEN_SIZE = (640, 480)


# === Initioal Processing ===
def init():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)	# view window
	pygame.display.set_caption(u"testてすと")


# === MAIN ===
def main():
	# init
	init()

	# loop
	while True:
		screen.fill((0, 0, 255))	# blue
		pygame.display.update()		# screen update
	
		# invent processing
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()


if __name__ == "__main__":
	main()


