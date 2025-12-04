DIGITS = 12
total = 0

with open("Input.txt") as f:
	for line in f:
		bank = line.strip()
		joltage = ""
		start = 0
		end = len(bank) - DIGITS + 1

		for _ in range(DIGITS):
			max_jolt = 0
			for i in range(start, end):
				jolt = int(bank[i])
				if jolt > max_jolt:
					max_jolt = jolt
					start = i
			joltage += bank[start]
			start += 1
			end += 1

		total += int(joltage)

print(total)
