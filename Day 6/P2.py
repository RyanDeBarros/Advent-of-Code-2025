lines = []
with open("Input.txt") as f:
	rows = sum(1 for _ in f) - 1
	f.seek(0)
	for _ in range(rows):
		lines.append(f.readline().rstrip())
	operations = f.readline().rstrip()


class Expression:
	def __init__(self, rows):
		self.nums = ["" for _ in range(rows)]
		self.op = ""

	def eval(self):
		if self.op.strip() == '*':
			val = 1
			for num in self.nums:
				val *= int(num.strip())
			return val
		elif self.op.strip() == '+':
			val = 0
			for num in self.nums:
				val += int(num.strip())
			return val
		else:
			return 0


line_width = max(max(len(line) for line in lines), len(operations)) + 1
for i in range(rows):
	lines[i] = lines[i].ljust(line_width)
operations = operations.ljust(line_width)

expressions = []
expression = Expression(0)
for cs in zip(*lines, operations):
	if all(c == ' ' for c in cs):
		expressions.append(expression)
		expression = Expression(0)
	else:
		expression.nums.append("".join(cs[:-1]))
		expression.op += cs[-1]

print(sum(exp.eval() for exp in expressions))
