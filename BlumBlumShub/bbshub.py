#Coded By B3mB4m
#M = p*q
#p != q
#s = [1,M-1]
#x0 = s*2 (mod M)
#Random numbers : x(n+1) = x(n)**2 mod M

import random
M = 9281*9973
s = random.randint(1, M-1) % M
x0 = s**2 % M

for number in xrange(0, 10):
	cache = x0 ** 2 % M
	x0 = cache
	print cache
