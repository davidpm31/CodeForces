if __name__ == '__main__':
	n, k = [int(i) for i in input().split()]
	print(len([i for i in input().split() if i.count('4') + i.count('7') <= k]))