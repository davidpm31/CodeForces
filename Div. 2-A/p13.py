if __name__ == '__main__':
	n = int(input())
	homeUni, guestUni, gamesBothGuest = [None] * n, [None] * n, 0
 
	for i in range(0, n):
		homeUni[i], guestUni[i] = [int(u) for u in input().split()]
 
	for i in range(0, n):
		gamesBothGuest = gamesBothGuest + guestUni.count(homeUni[i])
 
	print(gamesBothGuest)