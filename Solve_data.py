# It's copy of the Solver class, but for the 2D list
# We need it to get solved data without using Solver

def __init__(self, board):
	self.board = board

# Finding empty field where value must be put in
def find_empty_field(data):
	for x in range(9):
		for y in range(9):
			if (data[x][y] == 0):
				return (x,y)
	return None

# Checks if value that was picked, can be put in our empty field
def check(pos, value, data):
	# Check row
    for x in range(9):
        if data[pos[0]][x] == value and pos[1] != x:
            return False

    # Check column
    for x in range(9):
        if data[x][pos[1]] == value and pos[0] != x:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for x in range(box_y*3, box_y*3 + 3):
        for y in range(box_x * 3, box_x*3 + 3):
            if data[x][y] == value and (x, y) != pos:
                return False

    return True

def solve(data):
	pos = find_empty_field(data)
	if pos is None:
		return True

	x, y = pos

	for i in range(1, 10):
		if check(pos, i, data):
			delay = 20

			# If correct we set green color, update surface, wait for a while
			# set back to the primary color and again wait until we set to red
			data[x][y] = i

			if solve(data):
				return True

			# works same as for the correct value, but is set for color red
			# and incorrect value
			data[x][y] = 0


	return False