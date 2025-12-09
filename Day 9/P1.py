from itertools import combinations

red_tiles = [tuple(map(int, line.split(','))) for line in open("Input.txt")]
print(max((abs(t2[0] - t1[0]) + 1) * (abs(t2[1] - t1[1]) + 1) for t1, t2 in combinations(red_tiles, 2)))
