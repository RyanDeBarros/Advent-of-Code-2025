import math


def is_invalid_by_div(string, divisor):
	sublength = len(string) // divisor
	return divisor != 1 and all(string[i * sublength: (i + 1) * sublength] == string[(i + 1) * sublength: (i + 2) * sublength] for i in range(divisor - 1))


def is_invalid(string):
	return any(len(string) % divisor == 0 and (is_invalid_by_div(string, divisor) or is_invalid_by_div(string, len(string) // divisor)) for divisor in range(1, int(math.sqrt(len(string))) + 1))


print(sum(sum(filter(lambda num: is_invalid(str(num)), range(int(r.split('-')[0]), int(r.split('-')[1]) + 1))) for r in open("Input.txt").readline().split(',')))
