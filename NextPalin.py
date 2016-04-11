'''In this kata you will be given a positive integer, val and you have 
to create the function next_pal()(nextPal Javascript) that will output the 
smallest palindrome number higher than val.'''

'''
import sys
sys.setrecursionlimit(1000)

	
#Recursive
def next_Pal(x):
	y = str(x+1)
	if y == y[::-1]:
		return int(y)
	else:
		return next_Pal(x+1)
'''		
#iterative

#This bit test if palindrome
def isPal(x):
	return str(x) == str(x)[::-1]

def next_Pal(val):
    val += 1
    while not isPal(val):
        val += 1
    return val


#This is a super simple version.

def nextpal(x):
while str(x+1) != str(x+1)[::-1]:
x+=1
return x+1

print next_Pal(11)
print next_Pal(188)
print next_Pal(191)
print next_Pal(2541)
print next_Pal(338862)



		