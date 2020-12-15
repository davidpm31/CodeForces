if __name__ == '__main__':
	r, c = [int(i) for i in input().split()]
	evilStrawberryColum, evilStrawberryRow,  cakeStrings = set(), set(), []
	for i in range(0, r):
		cakeStrings.append(input())
		if cakeStrings[i].count('S'):
			[(evilStrawberryRow.add(i) , evilStrawberryColum.add(j)) for j in range(0, c) if cakeStrings[i][j] == 'S']
	pieces = r * c - len(evilStrawberryRow) * len(evilStrawberryColum)
	print(pieces)