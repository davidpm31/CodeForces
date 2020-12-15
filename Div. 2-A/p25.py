if __name__ == '__main__':
	n, m = [int(i) for i in input().split()]
	prevSteps, leftSteps = n // 2, n % 2
	while (prevSteps + leftSteps) % m:
		prevSteps = prevSteps - 1
		leftSteps = n - 2 * prevSteps
	if prevSteps >= 0 and leftSteps >= 0: print(prevSteps + leftSteps)
	else: print(-1)