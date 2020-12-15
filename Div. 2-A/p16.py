if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    puzzleList = [int(i) for i in input().split()]
    puzzleList.sort()
    minSub = max(puzzleList)
    for i in range(0, m - n + 1):
        aux = max(puzzleList[i:n+i]) - min(puzzleList[i:n+i])
        minSub = min(aux, minSub)
	print(minSub)