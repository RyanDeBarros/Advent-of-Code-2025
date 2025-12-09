from itertools import combinations
from shapely.geometry import Polygon, box

red_tiles = [tuple(map(int, line.split(','))) for line in open("Input.txt")]
polygon = Polygon(red_tiles)

print(max((abs(t2[0] - t1[0]) + 1) * (abs(t2[1] - t1[1]) + 1) for t1, t2 in combinations(red_tiles, 2)
		  if polygon.contains(box(min(t1[0], t2[0]), min(t1[1], t2[1]), max(t1[0], t2[0]), max(t1[1], t2[1])))))
