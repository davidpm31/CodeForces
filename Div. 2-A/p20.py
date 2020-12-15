if __name__ == '__main__':
	n, k = [int(i) for i in input().split()]
	odd = n - n // 2
	if k <= odd:
		print(2 * k - 1)
	else:
		print(2 * (k - odd))