import re

connections = {m.group(1): m.group(2).split() for m in (re.match(r"(...): (.*)", line.strip()) for line in open("Input.txt"))}

count = 0
process = ['you']
while len(process) > 0:
	next_input = process.pop()
	if next_input != 'out':
		if next_input in connections:
			outputs = connections[next_input]
			process += outputs
	else:
		count += 1
print(count)
