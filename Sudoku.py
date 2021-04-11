import random
from Start import *


# Get data from a file depending on the level that user set
def get_data(level):
	if level == 1:
		line = random.choice(list(open(EASY_PATH)))
	elif level == 2:
		line = random.choice(list(open(MEDIUM_PATH)))
	elif level == 3:
		line = random.choice(list(open(HARD_PATH)))

	data = [[int(line[9*y+x]) for x in range(9)] for y in range(9)]

	return data

# Draw timer 
def draw_timer(surface, time):
	font = pygame.font.Font(FONT_PATH_TEXT, 60)
	minutes = str((time//60000))
	seconds = str((time%60000)//1000)

	timer = "%s:%s" % (minutes, seconds)
	text = font.render(timer, True, (0, 0, 0))
	textRect = text.get_rect()
	textRect.center = (780, 860)

	surface.blit(text, textRect)

# Function controls every key input during game
def Key_controller(event_key, marked_cube, surface):
	# If cube is marked we change value of the field to a chosen number
	if event_key == pygame.K_1 and marked_cube is not None:
		marked_cube.value = 1
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_2 and marked_cube is not None:
		marked_cube.value = 2
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_3 and marked_cube is not None:
		marked_cube.value = 3
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_4 and marked_cube is not None:
		marked_cube.value = 4
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_5 and marked_cube is not None:
		marked_cube.value = 5
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_6 and marked_cube is not None:
		marked_cube.value = 6
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_7 and marked_cube is not None:
		marked_cube.value = 7
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_8 and marked_cube is not None:
		marked_cube.value = 8
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_9 and marked_cube is not None:
		marked_cube.value = 9
		marked_cube = marked_cube.unselect_cube(surface)
	elif event_key == pygame.K_ESCAPE and marked_cube is not None:
		marked_cube = marked_cube.unselect_cube(surface)

	return marked_cube

# After clicking check button we show end view
def end(board, time, score, level):
	font = pygame.font.Font(FONT_PATH_TEXT, 60)

	# Creating text with played time
	minutes = str((time//60000))
	seconds = str((time%60000)//1000)
	text = "%s:%s" % (minutes, seconds)
	time_text = font.render(text, True, (0, 0, 0))
	time_textRect = time_text.get_rect()
	time_textRect.topleft = (10, 835)

	# Creating text with ending score
	text = str(score) + "/100%"
	score_text = font.render(text, True, (0, 0, 0))
	score_textRect = score_text.get_rect()
	score_textRect.topleft = (time_textRect.right+20, 835)

	# Creating text with game level
	if level == 1:
		text = "Level: Easy"
	elif level == 2:
		text = "Level: Medium"
	elif level == 3:
		text = "Level: Hard"
	level_text = font.render(text, True, (0, 0, 0))
	level_textRect = level_text.get_rect()
	level_textRect.topleft = (score_textRect.right+20, 835)

	# Creating quit button
	quit_button = Button(board.surface, "QUIT", 700, 835, 50, 120, FONT_PATH_TEXT, 60)

	while True:
		# Drawing everything
		board.surface.fill((255, 255, 255))
		board.draw()
		quit_button.draw_button()
		board.surface.blit(time_text, time_textRect)
		board.surface.blit(score_text, score_textRect)
		board.surface.blit(level_text, level_textRect)
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# After clicking quit button we go back to start view
				if quit_button.rect.collidepoint(pygame.mouse.get_pos()):
					return True


# MAIN GAME
def main(level):
	# Creating surface and getting start time
	surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))
	time = pygame.time.get_ticks()

	# Load data
	data = get_data(level)

	# Creating board and solver
	board = Board(surface, data)
	solver = Solver(board)

	# Creating buttons
	check_button = Button(surface, "Check", 10, 835, 50, 120, FONT_PATH_TEXT, 60)
	reset_button = Button(surface, "Reset", 140, 835, 50, 120, FONT_PATH_TEXT, 60)
	solve_button = Button(surface, "Solve", 270, 835, 50, 120, FONT_PATH_TEXT, 60)

	# Variable that will hold an object (after clicking cube) in which we will change number
	marked_cube = None

	while(True):

		# Drawing everything
		surface.fill((255, 255, 255))
		board.draw()
		check_button.draw_button()
		reset_button.draw_button()
		solve_button.draw_button()

		# We take time from start of the main func and we substract 
		# with total time to get time during game
		draw_timer(surface, pygame.time.get_ticks()-time)
		pygame.display.update()

		# Event controller
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:

				# If clicked on reset button, reset board to the starting point
				if reset_button.rect.collidepoint(pygame.mouse.get_pos()):
					board.reset()
				# If clicked on solve button, we resert board and solve it
				elif solve_button.rect.collidepoint(pygame.mouse.get_pos()):
					board.reset()
					solver.solve()
				# If clicked on check button, we get score and show end view
				elif check_button.rect.collidepoint(pygame.mouse.get_pos()):
					score = board.check()
					return end(board, pygame.time.get_ticks()-time, score, level)
					
				for x in board.cubes:
					for cube in x:
						if cube.rect.collidepoint(pygame.mouse.get_pos()):
							# If cube was clicked we mark it as clicked
							if marked_cube is not None:
								marked_cube = marked_cube.unselect_cube(surface)
								marked_cube = cube.select_cube(surface)
							else:
								marked_cube = cube.select_cube(surface)
			elif event.type == pygame.KEYDOWN:
				marked_cube = Key_controller(event.key, marked_cube, surface)

if __name__ == "__main__":
	while True:
		level = start()
		if level is not None:
			if main(level) is None:
				break
		else:
			break
