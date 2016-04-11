'''Description: Write a program that will calculate the 
number of trailing zeros in a factorial of a given number.
N! = 1 * 2 * 3 * 4 ... N'''



def zeros(n):
	x = 0
	i = 5
	while n//i > 0:
		x += n//i
        i*=5
	return x



