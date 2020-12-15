#!/usr/bin/python3
 
if __name__ == '__main__':
	s = input()
	first = 0
	last = 0
	s = s.replace('WUB', ' ')
 
 
	s = s.split()
	s = ' '.join(s)
 
	print(s, sep = ' ')