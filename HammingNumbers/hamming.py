#Coded By B3mB4m
def hamming(number):
	if number == 1:
		return 1
	else:
		for x in [2,3,5]:
			if number % x == 0:
				return hamming(number/x)
for x in xrange(1, 60):
	if hamming( x) == 1: 
		print x
