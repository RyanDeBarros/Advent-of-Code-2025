with open("Input.txt") as f:
	beams = [c == 'S' for c in f.readline().strip()]

	total_splits = 0
	for line in f:
		new_beams = [False for _ in range(len(beams))]
		i = 0
		for c in line.strip():
			if beams[i]:
				if c == '^':
					total_splits += 1
					new_beams[i - 1] = True
					new_beams[i + 1] = True
				else:
					new_beams[i] = True
			i += 1
		beams = new_beams

print(total_splits)
