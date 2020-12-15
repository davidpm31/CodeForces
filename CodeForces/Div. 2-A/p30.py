if __name__ == '__main__':
	n, k = [int(i) for i in input().split()]
	validMembers = [int(i) for i in input().split() if int(i) + k <= 5]
	print(len(validMembers) // 3)