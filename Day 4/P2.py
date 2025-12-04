grid = [[c for c in line.strip()] for line in open("Input.txt")]


def is_accessible_roll(x: int, y: int):
	if grid[y][x] != '@':
		return False
	rolls = 0
	for ny in range(max(y - 1, 0), min(y + 2, len(grid))):
		for nx in range(max(x - 1, 0), min(x + 2, len(grid[ny]))):
			if not (nx == x and ny == y) and grid[ny][nx] == '@':
				rolls += 1
	return rolls < 4


total = 0

while True:
	step = 0
	new_grid = []
	for y in range(len(grid)):
		new_grid.append([])
		for x in range(len(grid[y])):
			if is_accessible_roll(x, y):
				step += 1
				new_grid[-1].append('x')
			else:
				new_grid[-1].append(grid[y][x])
	grid = new_grid
	if step == 0:
		break
	else:
		total += step

print(total)
