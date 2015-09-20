#Coded By B3mB4m
#Between 1-100 prime numbers .. 
for x in xrange(1, 100):
	if len([y for y in range(2,x)  if x%y == 0]) == 0:
		print x
