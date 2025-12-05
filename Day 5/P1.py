import re
from RangeMerger import merge_ranges, ranges_contain

sections = [[]]
with open("Input.txt") as f:
	for line in f:
		if line.strip() == "":
			sections.append([])
		else:
			sections[-1].append(line.strip())


fresh_ingredients = merge_ranges(map(lambda m: (int(m.group(1)), int(m.group(2))), [re.match(r"(\d+)-(\d+)", r) for r in sections[0]]))
print(len([ingredient for ingredient in sections[1] if ranges_contain(fresh_ingredients, int(ingredient))]))
