from Classes import *

# View after clicking level button
# We can change level there
def change_level(surface, sign):

	# Creating 3 buttons for 3 levels
	easy_button = Button(surface, "Easy", 265, 250, 80, 300, FONT_PATH_TEXT, 70)
	medium_button = Button(surface, "Medium", 265, 350, 80, 300, FONT_PATH_TEXT, 70)
	hard_button = Button(surface, "Hard", 265, 450, 80, 300, FONT_PATH_TEXT, 70)
	while(True):
		# Drawing everything
		surface.fill((255, 255, 255))
		sign.draw_button()
		easy_button.draw_button()
		medium_button.draw_button()
		hard_button.draw_button()
		pygame.display.update()

		# If button is clicked level is changed and returned
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

# Function that is created to show long text with multiple lines like two below
def blit_text(surface, text, x, y):
	font = pygame.font.Font(FONT_PATH_INFO, 25)
	for line in text.splitlines():
		note = font.render(line, True, (0, 0, 0))
		noteRect = note.get_rect()
		noteRect.midtop = (x, y)
		surface.blit(note, noteRect)
		y += 25


# View after clicking info button
def info(surface, sign):

	# Initializing text that will be showed and creating buttons
	htp_text = """Sudoku is played on a grid of 9 x 9 spaces.
	Within the rows and columns are 9 “squares”
	(made up of 3 x 3 spaces). Each row, column and
	square (9 spaces each) needs to be filled out with
	the numbers 1-9, without repeating any numbers within
	 the row, column or square."""

	info_text = """Click a box and hit the number on your
	keyboard to fill field with your number. After filling
	all numbers (or not if you can't figure that out) press
	"Check" button to see your score in the bottom left corner
	as a percentage (score = correct/every field that had to be
	filled). During	game you can also reset grid to the primary
	state by clicking "Reset" button or see how computer solves
	 it for you by clicking "Solve" button."""

	htp_sign = Button(surface, "How to play", 265, 215, 80, 300, FONT_PATH_TEXT, 70, True)
	info_sign = Button(surface, "Instructions", 265, 470, 80, 300, FONT_PATH_TEXT, 70, True)
	back_button = Button(surface, "Back", 265, 780, 80, 300, FONT_PATH_TEXT, 70)

	while(True):
		# Drawing everything
		surface.fill((255, 255, 255))
		sign.draw_button()
		htp_sign.draw_button()
		blit_text(surface, htp_text, 415, 305)
		info_sign.draw_button()
		blit_text(surface, info_text, 415, 560)
		back_button.draw_button()
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.rect.collidepoint(pygame.mouse.get_pos()):
					return


# START LOOP
def start():
	# Creating start display
	level = 1
	surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))

	# Creating buttons
	sudoku_sign = Button(surface, "Sudoku", 65, 50, 150, 700, FONT_PATH_SIGN, 190, True)
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
				# Start button
				# Start main game
				if start_button.rect.collidepoint(pygame.mouse.get_pos()):
					return level
				# Info button
				# Start info view
				elif info_button.rect.collidepoint(pygame.mouse.get_pos()):
					if info(surface, sudoku_sign):
						return
				# Quit button
				elif quit_button.rect.collidepoint(pygame.mouse.get_pos()):
					return
				# Level button
				# Start change level view
				elif level_button.rect.collidepoint(pygame.mouse.get_pos()):
					level = change_level(surface, sudoku_sign)
					if level != None:
						# Set string depending on number bcs it is much easier
						# than making if statements in Button class
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