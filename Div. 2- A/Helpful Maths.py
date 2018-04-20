#!/usr/bin/python3

if __name__ == '__main__':
	cad = input()

	tmp = sorted(cad)
	n = tmp.count('+')
	
	for i in range(0, n):
		tmp.remove('+')

	print('+'.join(tmp))
