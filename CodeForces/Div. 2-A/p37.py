if __name__ == '__main__':
	n, k, l, c, d, p, nl, np = [int(i) for i in input().split()]
	totalDrink, totalSlices = k * l, c * d
	totalToast = min(totalDrink // nl, totalSlices, p // np) // n
	print(totalToast)
	