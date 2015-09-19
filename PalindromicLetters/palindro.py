import itertools
import string
#Coded By B3mB4m
#For 4Char
for x in xrange(4,5): 
	for y in  list(itertools.product(string.ascii_lowercase, repeat=x)):
		if "".join(y) == "".join(y)[::-1]:
			print "".join(y)
