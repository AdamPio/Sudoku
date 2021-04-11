import pygame
import os
from Solve_data import *

# STATIC VARIABLES
pygame.init()
pygame.display.set_caption("Sudoku")
SCREEN_HIGH = 900
SCREEN_WIDTH = 830
FONT_PATH_INFO = os.path.join('Fonts', "ArchitectsDaughter-Regular.ttf")
FONT_PATH_SIGN = os.path.join("Fonts", "Bombing.ttf")
FONT_PATH_TEXT = os.path.join("Fonts", "leaves_and_ground.ttf")
EASY_PATH = os.path.join('data', 'Easy.txt')
MEDIUM_PATH = os.path.join('data', 'Medium.txt')
HARD_PATH = os.path.join('data', 'Hard.txt')

# Classes
#################################################################################################################
class Board:
	def __init__(self, surface, data):
		self.data = data
		# Get surface
		self.surface = surface
		# Create list of objects of class Cube
		self.cubes = self.get_cubes()
		# Draw board
		self.draw()

	# Create 2D list of objects of Cube class
	def get_cubes(self):
		cubes = [[Cube(self.surface, self.data[y][x], x, y) for x in range(9)] for y in range(9)]
		return cubes


	def draw(self):
		# Thick lines
		for x in range(10, 830, 270):
			pygame.draw.line(self.surface, (0, 0, 0), (10, x), (830 - 10, x), 3)
		for y in range(10, 830, 270):
			pygame.draw.line(self.surface, (0, 0, 0), (y, 10), (y, 830 - 10), 3)

		# Fine lines
		for x in range(10, 830, 90):
			pygame.draw.line(self.surface, (0, 0, 0), (10, x), (830 - 10, x), 1)
		for y in range(10, 830, 90):
			pygame.draw.line(self.surface, (0, 0, 0), (y, 10), (y, 830 - 10), 1)

		# Drawing cubes
		for x in self.cubes:
			for cube in x:
				cube.draw_value(self.surface)

	# Resetting values of board to a primary state
	def reset(self):
		i = 0
		for x in self.cubes:
			j = 0
			for cube in x:
				cube.value = self.data[i][j]
				j += 1
			i += 1

	def check(self):
		# Getting copy of our data
		solved_data = [x[:] for x in self.data]
		score = 0
		total = 0

		# Solving copy of our data
		solve(solved_data)
		# Comparing every field
		for x in range(9):
			for y in range(9):
				# 
				if self.cubes[x][y].changeable == True:
					if solved_data[x][y] == self.cubes[x][y].value:
						self.cubes[x][y].color = (0, 150, 0)
						self.cubes[x][y].changeable = False
						score += 1
					else:
						self.cubes[x][y].color = (150, 0, 0)
						self.cubes[x][y].changeable = False
					total += 1
		return int((score/total)*100)


#################################################################################################################
# To check documentation go to "Solve_data.py"
# Only difference is that it changes values live on board
class Solver:
	def __init__(self, board):
		self.board = board

	def find_empty_field(self):
		for x in range(9):
			for y in range(9):
				if (self.board.cubes[x][y].value == 0):
					return (x,y)
		return None

	def check(self, pos, value):
	    for x in range(9):
	        if self.board.cubes[pos[0]][x].value == value and pos[1] != x:
	            return False

	    for x in range(9):
	        if self.board.cubes[x][pos[1]].value == value and pos[0] != x:
	            return False

	    box_x = pos[1] // 3
	    box_y = pos[0] // 3

	    for x in range(box_y*3, box_y*3 + 3):
	        for y in range(box_x * 3, box_x*3 + 3):
	            if self.board.cubes[x][y].value == value and (x, y) != pos:
	                return False

	    return True

	def solve(self):
		pos = self.find_empty_field()
		if pos is None:
			return True

		x, y = pos

		for i in range(1, 10):
			if self.check(pos, i):
				delay = 20

				self.board.cubes[x][y].value = i
				self.board.cubes[x][y].color = (0, 150, 0)
				self.board.cubes[x][y].draw_value(self.board.surface)
				pygame.display.update()
				pygame.time.delay(delay)
				self.board.cubes[x][y].color = (180, 210, 180)
				self.board.cubes[x][y].draw_value(self.board.surface)
				pygame.display.update()
				pygame.time.delay(delay)

				if self.solve():
					return True

				self.board.cubes[x][y].value = 0
				self.board.cubes[x][y].color = (150, 0, 0)
				self.board.cubes[x][y].draw_value(self.board.surface)
				pygame.display.update()
				pygame.time.delay(delay)
				self.board.cubes[x][y].color = (180, 210, 180)
				self.board.cubes[x][y].draw_value(self.board.surface)
				pygame.display.update()
				pygame.time.delay(delay)

		return False

#################################################################################################################
class Cube:
	def __init__(self, surface, value, x, y):
		self.value = value
		self.rect = pygame.Rect(x*90+15, y*90+15, 80, 80)
		self.color = (180, 210, 180)
		# If value is 0 then it means that it is empty field
		# and as a user we can change that field
		if value == 0:
			self.changeable = True
		else:
			self.changeable = False

	# If user select cube to change its value we set another color
	# to make it more visible
	def select_cube(self, surface):
		if self.changeable == True:
			self.color = (255, 255, 120)
			pygame.draw.rect(surface, self.color, self.rect)
			self.draw_value(surface)
			return self

	# After changing, we set color to the primary state
	def unselect_cube(self, surface):
		self.color = (180, 210, 180)
		pygame.draw.rect(surface, self.color, self.rect)
		self.draw_value(surface)
		return None

	# Drawing value and cube
	def draw_value(self, surface):
		# everything is the same for both statments except
		# color of the text and of course we do not show 0
		if self.value == 0:
			text = ""
		else:
			text = str(self.value)
		font = pygame.font.Font(FONT_PATH_TEXT, 70)
		pygame.draw.rect(surface, self.color, self.rect)
		if self.changeable == False:
			text = font.render(text, True, (255, 255, 255))
			textRect = text.get_rect()
			textRect.center = self.rect.center
			surface.blit(text, textRect)
		else:
			text = font.render(text, True, (70, 70, 70))
			textRect = text.get_rect()
			textRect.center = self.rect.center
			surface.blit(text, textRect)

#################################################################################################################
class Button:
	def __init__(self, surface, text, x, y, h, w, font, size, sign =  False):
		self.rect = pygame.Rect(x, y, w, h)
		self.text = text
		self.font = font
		self.size = size
		self.surface = surface
		self.sign = sign

	def draw_button(self):
		# If it is sign we just want it to have one color
		if self.sign == True:
			color = (180, 210, 180)
		# If it is button
		else:
			# if mouse is hovered on a button, different color and different if it is not
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				color = (100, 210, 100)
			else:
				color = (180, 210, 180)

		pygame.draw.rect(self.surface, color, self.rect)
		points = [self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft]
		pygame.draw.lines(self.surface, (0, 0, 0), True, points, 3)

		font = pygame.font.Font(self.font, self.size)
		text = font.render(self.text, True, (255, 255, 255))
		textRect = text.get_rect()
		textRect.center = self.rect.center
		self.surface.blit(text, textRect)