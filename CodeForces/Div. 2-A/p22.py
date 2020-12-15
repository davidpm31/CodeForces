if __name__ == '__main__':
	n = int(input())
	print(n if n >= 0 else - min(abs(n) // 10, (abs(n) // 100) * 10 + abs(n) % 10))