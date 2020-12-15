if __name__ == '__main__':
	n = int(input())
	studentList = input().split()
	prog, math, pe = studentList.count('1'), studentList.count('2'), studentList.count('3')
	maxTeams = min(prog, math, pe)
	studentList = [(j, i) for i, j in zip(range(1, n + 1), studentList)]
	studentList = sorted(studentList)

	print(maxTeams)
	for i in range(0, maxTeams):
		print(f'{studentList[i][1]:d} {studentList[i + prog][1]:d} {studentList[i + math + prog][1]:d}')