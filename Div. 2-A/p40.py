if __name__ == '__main__':
	n = int(input())
	exeList = [int(i) for i in input().split()]
	ches, bice, back, i = 0, 0, 0, 0
	while i < n:
		if i < n: ches, i = (ches + exeList[i]), i + 1
		if i < n: bice, i = (bice + exeList[i]), i + 1
		if i < n: back, i = (back + exeList[i]), i + 1
		
	print('chest' if ches == max(ches, bice, back) else ('biceps' if bice == max(bice, back) else 'back'))