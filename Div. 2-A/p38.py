if __name__ == '__main__':
	a, b = [int(i) for i in input().split()]
	aWins, bWins, draws = 0, 0, 0
	for x in range(1, 7):
		if abs(a - x) < abs(b - x): aWins += 1
		elif abs(a - x) > abs(b - x): bWins += 1
		else: draws += 1
	print(aWins, draws, bWins)