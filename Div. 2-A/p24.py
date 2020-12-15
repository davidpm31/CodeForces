from bisect import insort

if __name__ == '__main__':
	strength, dragons = [int(i) for i in input().split()]
	dragonStrengthIncrease = []
	for i in range(0, dragons):
		auxd, auxi = [int(i) for i in input().split()]
		insort(dragonStrengthIncrease, (auxd, auxi))

	idx, actualDragon = 0, dragonStrengthIncrease[0][0]
	while actualDragon < strength and idx < dragons:
		strength += dragonStrengthIncrease[idx][1]
		actualDragon = dragonStrengthIncrease[idx + 1 if idx + 1 < dragons else idx][0]
		idx += 1
	print('YES' if idx == dragons else 'NO')
