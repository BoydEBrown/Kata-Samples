def compare_powers(n1,n2):
	p1 = n1[0]**n1[1]
	p2 = n2[0]**n2[1]
	if p1 == p2:
		return 0
	elif p1 < p2:
		return 1
	else:
		return -1

compare_powers([2,3],[4,2])

import math

def compare_powers(n1,n2):
	p1 = math.pow(n1[0],n1[1])
	p2 = math.pow(n2[0],n2[1])
	if p1 == p2:
		return 0
	elif p1 < p2:
		return 1
	else:
		return -1

compare_powers([2,3],[4,2])

import math

def compare_powers(n1,n2):
	p1 = n1[1]*math.log(n1[0])
	p2 = n2[1]*math.log(n2[0])
	if p1 == p2:
		return 0
	elif p1 < p2:
		return 1
	else:
		return -1

compare_powers([2,3],[4,2])