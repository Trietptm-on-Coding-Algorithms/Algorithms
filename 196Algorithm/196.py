import random
#Coded By B3mB4m
#196 Algorithm
number = random.randint(9, 999)

for x in xrange(1, 100):
	if str(number+int(str(number)[::-1])) == str(number+int(str(number)[::-1]))[::-1]:
		print "\tNumber found : %s" % str(number+int(str(number)[::-1]))
	else:
		print "Fail : %s" % str(number)
	number = number+int(str(number)[::-1])
