#!/usr/bin/python3

if __name__ == '__main__':
	n = int(input())

	for i in range(0, n):
		cad = input()
		aux = len(cad)
		if(aux > 10):
			print (cad[0] + str(aux - 2) + cad[aux - 1])
		else:
			print (cad)
