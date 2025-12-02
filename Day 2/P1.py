def is_invalid(string):
	length = len(string)
	return length & 1 == 0 and string[:length//2] == string[length//2:]


print(sum(sum(filter(lambda num: is_invalid(str(num)), range(int(r.split('-')[0]), int(r.split('-')[1]) + 1))) for r in open("Input.txt").readline().split(',')))
