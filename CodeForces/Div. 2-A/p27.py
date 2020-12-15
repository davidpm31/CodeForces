if __name__ == '__main__':
	n, d = [int(i) for i in input().split()]
	songList = [int(i) for i in input().split()]
	minRuntime = sum(songList) + 10 * (n - 1)
	if minRuntime > d: print(-1)
	else:
		print(2 * (n -1) + (d - minRuntime) // 5)