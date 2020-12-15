if __name__ == '__main__':
	n = int(input())
	holdList = [int(i) for i in input().split()]
	tmpList, minDif, maxDif = [], max(holdList), 0

	for i in range(1, n - 1):
		tmpList = holdList[:i] + holdList[i + 1:]
		for j in range(0, n - 2):
			maxDif = max(maxDif, tmpList[j + 1] - tmpList[j])
		minDif, maxDif = min(minDif, maxDif), 0
	print(minDif)