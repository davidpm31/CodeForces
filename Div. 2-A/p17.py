if __name__ == '__main__':
	a, b, c = int(input()), int(input()), int(input())
	resultList = [a+b+c, a+b*c, a*b+c, a*b*c, (a*b)*c, a*(b*c), (a+b)*c, a*(b+c)]
	print(max(resultList))