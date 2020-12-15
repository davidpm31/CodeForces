if __name__ == '__main__':
	n = int(input())
	coordList, superCentral = [], 0
	for i in range(0, n):
		coordList.append([int(i) for i in input().split()])

	for i in range(0, n):
		neighbors = [0] * 4
		for j in range(0, n):
			if coordList[j][0] > coordList[i][0] and coordList[j][1] == coordList[i][1]: neighbors[0] = 1
			if coordList[j][0] < coordList[i][0] and coordList[j][1] == coordList[i][1]: neighbors[1] = 1
			if coordList[j][0] == coordList[i][0] and coordList[j][1] < coordList[i][1]: neighbors[2] = 1
			if coordList[j][0] == coordList[i][0] and coordList[j][1] > coordList[i][1]: neighbors[3] = 1
		if sum(neighbors) == 4: superCentral += 1
	print(superCentral)
