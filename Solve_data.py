# It's copy of the Solver class, but for the 2D list
# We need it to get solved data without using Solver
# for our check function in Board class

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

# Solving sudoku using backtracking algorithm
def solve(data):
	# If we can't find empty field that means that every field was filled and board is solved
	pos = find_empty_field(data)
	if pos is None:
		return True

	x, y = pos

	# if not we find number that fits in empty field
	for i in range(1, 10):
		if check(pos, i, data):

			# if number is coorect, we set value in our field to that number
			data[x][y] = i

			# And by using recursion we check next empty field
			# if we get True (that happens only if there are not more fields to fill)
			# we return true to every other reference and ends
			if solve(data):
				return True

			# If we get False that means our number was incorrect and we change value to empty field again
			# and checking next value
			data[x][y] = 0

	return False