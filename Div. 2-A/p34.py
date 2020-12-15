if __name__ == '__main__':
	n, c = [int(i) for i in input().split()]
	kiloDays = [int(i) for i in input().split()]
	maxKilos = 0

	for i in range(0, n - 1):
		maxKilos = max(maxKilos, kiloDays[i] - kiloDays[i + 1] - c)

	print(maxKilos)