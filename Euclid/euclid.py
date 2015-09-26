#Coded By B3mB4m
#Euclid Algorithm
#I just convert C++ to Python on my book :P 

a = 396
b = 120
r = 0

while b != 0:
	r = a
	a = b
	b = r % b
print "Euclid : %d" % a
