if __name__ == '__main__':
	n, k = [int(i) for i in input().split()]
	maxJoy = - 10 ** 9
	for i in range(0, n):
		f, t = [int(i) for i in input().split()]
		if t <= k: maxJoy = max(maxJoy, f)
		else: maxJoy = max(maxJoy, f - t +  k)
	print(maxJoy)