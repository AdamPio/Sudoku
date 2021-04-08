import pygame
import os
from Classes import *

pygame.init()

# Changing diffulcty
def change_level(surface, sign):
	easy_button = Button(surface, "Easy", 265, 250, 80, 300, FONT_PATH_TEXT, 70)
	medium_button = Button(surface, "Medium", 265, 350, 80, 300, FONT_PATH_TEXT, 70)
	hard_button = Button(surface, "Hard", 265, 450, 80, 300, FONT_PATH_TEXT, 70)
	while(True):
		surface.fill((255, 255,255))
		sign.draw_button()
		easy_button.draw_button()
		medium_button.draw_button()
		hard_button.draw_button()
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if easy_button.rect.collidepoint(pygame.mouse.get_pos()):
					return 1
				elif medium_button.rect.collidepoint(pygame.mouse.get_pos()):
					return 2
				elif hard_button.rect.collidepoint(pygame.mouse.get_pos()):
					return 3

# START LOOP
def start():
	# Creating start display
	level = 1
	surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))

	# Creating buttons
	sudoku_sign = Button(surface, "Sudoku", 65, 50, 150, 700, FONT_PATH_SIGN, 190)
	start_button = Button(surface, "Start", 265, 250, 80, 300, FONT_PATH_TEXT, 70)
	level_button = Button(surface, "Level: Easy", 265, 350, 80, 300, FONT_PATH_TEXT, 70)
	info_button = Button(surface, "Info", 265, 450, 80, 300, FONT_PATH_TEXT, 70)
	quit_button = Button(surface, "Quit", 265, 550, 80, 300, FONT_PATH_TEXT, 70)

	while(True):
		# Drawing everything
		surface.fill((255, 255, 255))
		start_button.draw_button()
		sudoku_sign.draw_button()
		level_button.draw_button()
		info_button.draw_button()
		quit_button.draw_button()
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if start_button.rect.collidepoint(pygame.mouse.get_pos()):
					return level
				elif quit_button.rect.collidepoint(pygame.mouse.get_pos()):
					return
				elif level_button.rect.collidepoint(pygame.mouse.get_pos()):
					level = change_level(surface, sudoku_sign)
					if level != None:
						if level == 1:
							level_button.text = "Level: Easy"
						elif level == 2:
							level_button.text = "Level: Medium"
						elif level == 3:
							level_button.text = "Level: Hard"
					else:
						return


if __name__ == "__main__":
	start()