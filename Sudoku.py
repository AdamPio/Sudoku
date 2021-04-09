import random
from Start import *

# LOAD DATA

def get_data(level):
	if level == 1:
		line = random.choice(list(open(EASY_PATH)))
	elif level == 2:
		line = random.choice(list(open(MEDIUM_PATH)))
	elif level == 3:
		line = random.choice(list(open(HARD_PATH)))

	data = [[int(line[9*y+x]) for x in range(9)] for y in range(9)]

	return data


# FUNCTIONS

def draw_timer(surface, time):
	font = pygame.font.Font(FONT_PATH_TEXT, 60)
	minutes = str((time//60000))
	seconds = str((time%60000)//1000)

	timer = "%s:%s" % (minutes, seconds)
	text = font.render(timer, True, (0, 0, 0))
	textRect = text.get_rect()
	textRect.center = (780, 860)

	surface.blit(text, textRect)

def Key_controller(event_key, marked_cube, surface):
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

def end(board, time, score, level):
	# Getting time to show
	minutes = str((time//60000))
	seconds = str((time%60000)//1000)

	font = pygame.font.Font(FONT_PATH_TEXT, 60)

	# Time text init
	text = "%s:%s" % (minutes, seconds)
	time_text = font.render(text, True, (0, 0, 0))
	time_textRect = time_text.get_rect()
	time_textRect.topleft = (10, 835)

	# Score text init
	text = str(score) + "/100%"
	score_text = font.render(text, True, (0, 0, 0))
	score_textRect = score_text.get_rect()
	score_textRect.topleft = (time_textRect.right+20, 835)

	# Level text init
	if level == 1:
		text = "Level: Easy"
	elif level == 2:
		text = "Level: Medium"
	elif level == 3:
		text = "Level: Hard"
	level_text = font.render(text, True, (0, 0, 0))
	level_textRect = level_text.get_rect()
	level_textRect.topleft = (score_textRect.right+20, 835)

	quit_button = Button(board.surface, "QUIT", 700, 835, 50, 120, FONT_PATH_TEXT, 60)
	while True:
		board.surface.fill((255, 255, 255))
		board.draw()
		quit_button.draw_button()
		board.surface.blit(time_text, time_textRect)
		board.surface.blit(score_text, score_textRect)
		board.surface.blit(level_text, level_textRect)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if quit_button.rect.collidepoint(pygame.mouse.get_pos()):
					return True
		pygame.display.update()


# MAIN LOOP
def main(level):
	# Creating display
	surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))
	time = pygame.time.get_ticks()

	data = get_data(level)

	# Creating board and solver
	board = Board(surface, data)
	solver = Solver(board)

	# Creating buttons
	check_button = Button(surface, "Check", 10, 835, 50, 120, FONT_PATH_TEXT, 60)
	check = False
	reset_button = Button(surface, "Reset", 140, 835, 50, 120, FONT_PATH_TEXT, 60)
	solve_button = Button(surface, "Solve", 270, 835, 50, 120, FONT_PATH_TEXT, 60)

	# Variable that will hold an object (after clicking cube) in which we will change number
	marked_cube = None

	while(True):

		# Drawing everything that can be seen
		surface.fill((255, 255, 255))
		board.draw()
		check_button.draw_button()
		reset_button.draw_button()
		solve_button.draw_button()
		# We take time from start of the main func and we substract 
		#with total time to get time during game
		draw_timer(surface, pygame.time.get_ticks()-time)

		# Event controller
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# if clicked on reset button, reset board to the starting point
				if reset_button.rect.collidepoint(pygame.mouse.get_pos()):
					board.reset()
				elif solve_button.rect.collidepoint(pygame.mouse.get_pos()):
					print()
					board.reset()
					solver.solve()
				elif check_button.rect.collidepoint(pygame.mouse.get_pos()):
					score = board.check()
					# We get level from Start file
					return end(board, pygame.time.get_ticks()-time, score, level)
					
				for x in board.cubes:
					for cube in x:
						if cube.rect.collidepoint(pygame.mouse.get_pos()):
							if marked_cube is not None:
								marked_cube = marked_cube.unselect_cube(surface)
								marked_cube = cube.select_cube(surface)
							else:
								marked_cube = cube.select_cube(surface)
			elif event.type == pygame.KEYDOWN:
				marked_cube = Key_controller(event.key, marked_cube, surface)


		pygame.display.update()

if __name__ == "__main__":
	while True:
		level = start()
		if level is not None:
			if main(level) is None:
				break
		else:
			break
