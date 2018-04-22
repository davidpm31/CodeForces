#!/usr/bin/python3

if __name__ == '__main__':
	n = int(input())
	aux = str(n)

	aux = aux.replace('7', '')
	aux = aux.replace('4', '')

	if ((n % 4) == 0 or (n % 7) == 0 or (n % 44) == 0 or (n % 47) == 0 or (n % 74) == 0 or (n % 77) == 0 or (n % 444) == 0 or (n % 447) == 0 or (n % 474) == 0 or (n % 477) == 0 or len(aux) == 0):
		print('YES')
	else:
		print('NO')