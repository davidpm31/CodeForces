if __name__ == '__main__':
	setString = input()
	if len(setString) > 2: setString = set(setString[1:-1].split(', '))
	else: setString = []
	print(len(setString))