if __name__ == '__main__':
	n, m = [int(i) for i in input().split()]
	straightRow = '#' * m
	curvedRow = '.' * (m - 1) + '#'
	flag = 1
	for i in range(0, n):
		if i % 2:
			print(curvedRow[::flag])
			flag = flag * -1
		else: print(straightRow)