if __name__ == '__main__':
	n = int(input())
	diagSet, leftSet = set(), set()
	i, j = 0, n - 1
	for l in range(0, n):
		line = input()
		for c in range(0, n):
			if c == i or c == j:
				diagSet.add(line[c])
			else:
				leftSet.add(line[c])
		i, j = i + 1, j - 1
	print('YES' if len(diagSet) == 1 and len(leftSet) == 1 and len(leftSet - diagSet) == 1 else 'NO')