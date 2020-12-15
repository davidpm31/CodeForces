from math import ceil
if __name__ == '__main__':
	nRides, mRides, aRubles, bRubles = [int(i) for i in input().split()]
	total = min((aRubles * nRides), ceil(nRides / mRides) * bRubles, bRubles * (nRides // mRides) + aRubles * (nRides - (nRides // mRides) * mRides))
	print(total)