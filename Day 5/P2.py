import re
from itertools import takewhile
from RangeMerger import merge_ranges

print(sum(r[1] - r[0] + 1 for r in merge_ranges(map(lambda m: (int(m.group(1)), int(m.group(2))), [re.match(r"(\d+)-(\d+)", r) for r in takewhile(lambda line: line.strip() != "", open("Input.txt"))]))))
