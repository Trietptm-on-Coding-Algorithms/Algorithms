#Coded By B3mB4m
#C(n) = (2n)!/(n+1)!n! n => 0
#And we want first x10 number ..

def fac(number):
	return eval("*".join([str(x) for x in xrange(1,number+1)][::-1]))
	#https://github.com/b3mb4m/Algorithms/blob/master/factorial/fac.py

for n in xrange(1, 11):
	print fac( 2*n)/(fac( n+1)*fac( n)) 
