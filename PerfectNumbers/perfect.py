#Coded By B3mB4m
#Perfect Numbers

for number in xrange(1, 9999):
	if number == sum([x for x in xrange(1,number) if number % x == 0]):
		print "Perfect number : %d " % number
