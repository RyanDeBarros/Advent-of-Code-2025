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


print(sum(sum(int(is_accessible_roll(x, y)) for x in range(len(grid[y]))) for y in range(len(grid))))
