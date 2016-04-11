from itertools import groupby

def unique_in_order(iterable):
	old =[]
	l = iterable
	old += l
	new =[]

	new =[i[0] for i in groupby(old)]
	return new

unique_in_order('aaabbbcccdddaabbaaccaadd')
unique_in_order(['a','a','b','c','c','c','b','b','a','a'])

# defines function unique_in_order
def unique_in_order(iterable):
 # creates new (empty) list called result
    result = []
#Asssigns prev to none, or 'null/empty'
    prev = None
# for char in argument iterable range 0 to end of list...
    for char in iterable[0:]:
#if char does not equal empty...
        if char != prev:
# take that charater and append it to end of result list...
            result.append(char)
#assign prev to last char appended. yay!            
            prev = char
    return result