import re

import z3


def solve_fewest_presses(buttons, joltages):
	presses = [z3.Int(i) for i in range(len(buttons))]
	opt = z3.Optimize()

	for p in presses:
		opt.add(p >= 0)

	for j in range(len(joltages)):
		opt.add(sum(presses[b] for b, button in enumerate(buttons) if j in button) == joltages[j])

	sol = opt.minimize(sum(presses))
	opt.check()
	return opt.lower(sol).as_long()


def parse_line(line):
	m = re.match(r"\[(.*)] (.*) \{(.*)}", line.strip())
	configuration = list(map(lambda c: c == '#', m.group(1)))
	buttons = [list(map(int, button[1:-1].split(','))) for button in m.group(2).split()]
	joltages = list(map(int, m.group(3).split(',')))
	return configuration, buttons, joltages


print(sum(solve_fewest_presses(buttons, joltages) for _, buttons, joltages in [parse_line(line) for line in open("Input.txt")]))
