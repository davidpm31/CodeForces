if __name__ == '__main__':
	n, m = [int(i) for i in input().split()]
	classList, best = [], 0
	for i in range(0, n):
		classList.append([int(i) for i in list(input())])

	for i in range(0, n):
		prev = False
		for j in range(0, m):
			curr = True
			for k in range(0, n):
				if classList[k][j] > classList[i][j]: curr = False
			if curr: prev = True
		if prev: best += 1

	print(best)
