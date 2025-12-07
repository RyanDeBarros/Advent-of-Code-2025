class GraphNode:
	def __init__(self):
		self.parents: set[GraphNode] = set()
		self.children: set[GraphNode] = set()


with open("Input.txt") as f:
	START = GraphNode()
	latest = {f.readline().strip().index('S'): START}

	for line in f:
		new_latest: dict[int, GraphNode] = {}


		def update_latest(i, j):
			if j not in new_latest:
				new_latest[j] = GraphNode()
			new_latest[j].parents.add(latest[i])
			latest[i].children.add(new_latest[j])


		i = 0
		for c in line.strip():
			if i in latest:
				if c == '^':
					update_latest(i, i - 1)
					update_latest(i, i + 1)
				else:
					update_latest(i, i)
			i += 1
		latest = new_latest

counter = {START: 1}
process = START.children
while len(process) > 0:
	for node in process:
		counter[node] = sum(counter[parent] for parent in node.parents)

	for node in process:
		for parent in node.parents:
			counter.pop(parent, None)

	process = {child for node in process for child in node.children}

print(sum(counter.values()))
