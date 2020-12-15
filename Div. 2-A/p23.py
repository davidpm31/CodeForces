if __name__ == '__main__':
	x1, y1, x2, y2 = [int(i) for i in input().split()]
	if x1 != x2 and y1 != y2 and abs(x1 - x2) != abs(y1 - y2): print(-1)
	elif x1 == x2: print(f'{x1 + abs(y1 - y2) :d} {y1:d} {x2 + abs(y1 - y2):d} {y2:d}')
	elif y1 == y2: print(f'{x1:d} {y1 + abs(x1 - x2):d} {x2:d} {y2 + abs(x1 - x2):d}')
	else: print(f'{x1:d} {y2:d} {x2:d} {y1:d}')