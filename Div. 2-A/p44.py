if __name__ == '__main__':
	n, x = [int(i) for i in input().split()]
	totalMinutes, idx = 0, 1
	for i in range(0, n):
		l, r = [int(i) for i in input().split()]
		totalMinutes += (r - l + 1) + (l - idx) % x
		idx = r + 1
	print(totalMinutes)