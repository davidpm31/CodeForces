if __name__ == '__main__':
	n = int(input())
	table, adj, flag = ['x' * (n + 1)], 0, True

	for i in range(0, n):
		table.append('x' + input() + 'x')
	table.append('x' * (n + 1))

	for i in range(1, n + 1):
		if not flag: break
		for j in range(1, n + 1):
			if ((table[i + 1][j], table[i][j + 1], table[i - 1][j], table[i][j - 1]).count('o')) % 2:
				print('NO')
				flag = False
				break
	if flag: print('YES')