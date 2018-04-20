#!/usr/bin/python3

if __name__ == '__main__':
	A = input()
	B = input()

	if (A.lower() == B.lower()):
		print('0')
	elif (A.lower() < B.lower()):
		print('-1')
	elif (A.lower() > B.lower()):
		print('1')
