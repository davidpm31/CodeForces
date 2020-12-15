if __name__ == '__main__':
	n = int(input())
	laptopList = []

	for i in range(0, n):
		laptopList.append([int(i) for i in input().split()])

	laptopList.sort()
	sortedByQuality = sorted(laptopList, key = lambda x:x[1])
	print('Poor Alex' if sortedByQuality == laptopList else 'Happy Alex')