if __name__ == '__main__':
	n, m = [int(i) for i in input().split()]
	correctList = [int(i) for i in input().split()]
	wrongList = [int(i) for i in input().split()]
	TL = -1
	for i in range(max(correctList), min(wrongList)):
		if 2 * min(correctList) <= i and i < min(wrongList):
			TL = i
			break
	print(TL) 