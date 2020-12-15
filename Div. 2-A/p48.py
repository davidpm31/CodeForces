def find(n, cuts):
	dp = [0] * (n + 1)
	for i in range(1, n + 1):
		a, b, c = -1, -1, -1
		if i >= cuts[0]: a = dp[i - cuts[0]]
		if i >= cuts[1]: b = dp[i - cuts[1]]
		if i >= cuts[2]: c = dp[i - cuts[2]]
		if a == -1 and b == -1 and c == -1: dp[i] = -1	
		else: dp[i] = max(a, b, c) + 1
	return dp[n]
if __name__ == '__main__':
	n, a, b, c = [int(i) for i in input().split()]
	print(find(n, [a, b, c]))