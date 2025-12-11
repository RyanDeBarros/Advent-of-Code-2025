import re
from collections import defaultdict

connections = defaultdict(set)
with open("Input.txt") as f:
	for line in f:
		m = re.match(r"(...): (.*)", line.strip())
		for o in m.group(2).split():
			connections[o].add(m.group(1))

def dfs(start, end, memo=None):
	if start == end:
		return 1
	if memo is None:
		memo = {}
	if start in memo:
		return memo[start]

	count = sum(dfs(next_input, end, memo) for next_input in connections[start])
	memo[start] = count
	return count

req1 = 'dac'
req2 = 'fft'

if dfs(req1, req2) == 0:
	req1, req2 = req2, req1

print(dfs('out', req1) * dfs(req1, req2) * dfs(req2, 'svr'))
