if __name__ == '__main__':
	n = int(input())
	numbersList = [int(i) % 2 for i in input().split()]
	print(numbersList.index(1) + 1 if numbersList.count(1) == 1 else numbersList.index(0) + 1)