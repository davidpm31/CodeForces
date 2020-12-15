if __name__ == '__main__':
	n, v = [int(i) for i in input().split()]
	sellerList = []
	for i in range(0, n):
		sellerList.append([int(i) for i in input().split()])

	sellerDealList = []
	for i, j in enumerate(sellerList):
		if v > min(j[1:]): sellerDealList.append(str(i + 1))

	print(f'{len(sellerDealList):d}\n{" ".join(sellerDealList):s}')