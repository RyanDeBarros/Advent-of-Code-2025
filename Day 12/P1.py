import re
from copy import deepcopy

class Shape:
	def __init__(self, grid):
		self.grid = grid

	def rotated_right(self):
		grid = deepcopy(self.grid)
		grid[0][0], grid[0][2], grid[2][2], grid[2][0] = grid[2][0], grid[0][0], grid[0][2], grid[2][2]
		grid[0][1], grid[1][2], grid[2][1], grid[1][0] = grid[1][0], grid[0][1], grid[1][2], grid[2][1]
		return Shape(grid)

	def rotated_left(self):
		grid = deepcopy(self.grid)
		grid[0][0], grid[0][2], grid[2][2], grid[2][0] = grid[0][2], grid[2][2], grid[2][0], grid[0][0]
		grid[0][1], grid[1][2], grid[2][1], grid[1][0] = grid[1][2], grid[2][1], grid[1][0], grid[0][1]
		return Shape(grid)

	def flipped_x(self):
		grid = deepcopy(self.grid)
		for i in range(3):
			grid[i][0], grid[i][2] = grid[i][2], grid[i][0]
		return Shape(grid)

	def flipped_y(self):
		grid = deepcopy(self.grid)
		grid[0], grid[2] = grid[2], grid[0]
		return Shape(grid)

	def area(self):
		return sum(sum(g) for g in self.grid)


class Region:
	def __init__(self, size, coefficients):
		self.size = size
		self.coefficients = coefficients

	def can_fit(self, shapes):
		if sum(shapes[i].area() * self.coefficients[i] for i in range(len(shapes))) > self.size[0] * self.size[1]:
			return False
		return sum(self.coefficients) * 9 <= self.size[0] * self.size[1]


shapes = []
regions = []
with open("Input.txt") as f:
	for _ in range(6):
		grid = [[False for _ in range(3)] for _ in range(3)]
		f.readline()  # skip N:
		for i in range(3):
			line = f.readline()
			for j in range(3):
				grid[i][j] = line[j] == '#'
		f.readline()  # skip \n
		shapes.append(Shape(grid))

	for line in f:
		m = re.match(r"(\d+)x(\d+): (.*)", line.strip())
		regions.append(Region((int(m.group(1)), int(m.group(2))), list(map(int, m.group(3).split()))))

print(sum(int(r.can_fit(shapes)) for r in regions))
