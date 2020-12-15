def points(p, t):
	return max(3 * p / 10, p - ((p / 250) * t))

if __name__ == '__main__':
	a, b, c, d = [int(i) for i in input().split()]
	print('Misha' if points(a, c) > points(b, d) else 'Tie' if points(a, c) == points(b, d) else 'Vasya')