import re

dial = 50
password = 0

with open("Input.txt") as f:
	for line in f:
		m = re.match(r"([LR])(\d+)", line.strip())
		num = int(m.group(2))

		if m.group(1) == 'R':
			password += (dial + num) // 100
		else:
			num = -num
			if dial + num <= 0:
				password += int(dial != 0) + abs(dial + num) // 100

		dial = (dial + num) % 100

print(password)
