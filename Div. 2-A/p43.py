if __name__ == '__main__':
	n = int(input())
	if n % 2: print(-1)
	else:
		for i in range(1, n + 1):
			print(i + 1 if i % 2 else i - 1, end = ' ')