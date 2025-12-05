import bisect

def merge_ranges(ranges):
	if not ranges:
		return []

	ranges = sorted(ranges)
	merged = [ranges[0]]

	for start, end in ranges[1:]:
		last_start, last_end = merged[-1]
		if start <= last_end:
			merged[-1] = (last_start, max(last_end, end))
		else:
			merged.append((start, end))

	return merged

def ranges_contain(ranges, key):
	idx = bisect.bisect_left(ranges, (key,))
	return (idx > 0 and ranges[idx - 1][1] >= key) or (idx < len(ranges) and ranges[idx][0] == key)
