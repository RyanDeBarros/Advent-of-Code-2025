total = 0

with open("Input.txt") as f:
	for line in f:
		bank = line.strip()
		joltage = 0
		for i in range(len(bank) - 1):
			for j in range(i + 1, len(bank)):
				jolts = int(bank[i] + bank[j])
				if jolts > joltage:
					joltage = jolts
		total += joltage

print(total)
