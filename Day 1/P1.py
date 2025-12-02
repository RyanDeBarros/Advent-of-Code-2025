import re

dial = 50
password = 0

with open("Input.txt") as f:
	for line in f:
		m = re.match(r"([LR])(\d+)", line.strip())
		num = int(m.group(2))

		if m.group(1) == 'L':
			num = -num

		dial = (dial + num) % 100
		if dial == 0:
			password += 1

print(password)
