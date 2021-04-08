import random

myline = random.choice(list(open("Easy.txt")))

# print(myline)

data = [[myline[9*y+x] for x in range(9)] for y in range(9)]

for line in data:
	for x in line:
		print(x, end=" ")
	print()
