import random
#Steinhaus Cyclus 
#Coded By B3mB4m
number = random.randint(999, 9999)
for i in xrange(1, 100):
	tmp = sum([int(x)*int(x) for x in str(number)])
	print tmp,
	number = tmp
