def triangle_type(a, b, c):
	tri = [a,b,c]
	sorted(tri)
	tri.sort()
	if tri[0] + tri[1] <= tri[2]:
		return 0
	elif tri[0]**2 + tri[1]**2 > tri[2]**2:
		return 1
	elif tri[0]**2 + tri[1]**2 == tri[2]**2:
		return 2
	else:
		return 3 
	
triangle_type(7,4,5)

