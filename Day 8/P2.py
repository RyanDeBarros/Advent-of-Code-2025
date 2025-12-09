import re
from itertools import combinations


def distance(t1, t2):
	return (t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2 + (t2[2] - t1[2]) ** 2


junctions = []
with open("Input.txt") as f:
	for line in f:
		m = re.match(r"(\d+),(\d+),(\d+)", line.strip())
		junctions.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

junction_pairs = sorted(combinations(junctions, 2), key=lambda t: distance(t[0], t[1]), reverse=True)

circuits = [{j} for j in junctions]
while True:
	j1, j2 = junction_pairs.pop()
	c1, c2 = -1, -1
	for i in range(len(circuits)):
		if j1 in circuits[i]:
			c1 = i
		if j2 in circuits[i]:
			c2 = i

	if c1 == -1:
		if c2 == -1:
			circuits.append({j1, j2})
		else:
			circuits[c2].add(j1)
	else:
		if c2 == -1:
			circuits[c1].add(j2)
		elif c1 != c2:
			circuits[c1].update(circuits[c2])
			circuits.pop(c2)

	if len(circuits) == 1:
		print(j1[0] * j2[0])
		break
