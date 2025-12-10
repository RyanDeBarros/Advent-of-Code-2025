import itertools
import re


def presses_passes(configuration, buttons, presses):
	for tup in itertools.product(range(len(buttons)), repeat=presses):
		result = [False for _ in range(len(configuration))]
		for i in tup:
			for b in buttons[i]:
				result[b] = not result[b]
		if result == configuration:
			return True
	return False


def fewest_presses(configuration, buttons):
	return next(presses for presses in itertools.count(1) if presses_passes(configuration, buttons, presses))


def parse_line(line):
	m = re.match(r"\[(.*)] (.*) \{(.*)}", line.strip())
	configuration = list(map(lambda c: c == '#', m.group(1)))
	buttons = [list(map(int, button[1:-1].split(','))) for button in m.group(2).split()]
	joltages = list(map(int, m.group(3).split(',')))
	return configuration, buttons, joltages


print(sum(fewest_presses(configuration, buttons) for configuration, buttons, _ in [parse_line(line) for line in open("Input.txt")]))
