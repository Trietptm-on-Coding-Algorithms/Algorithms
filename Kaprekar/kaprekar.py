#Coded By B3mB4m
#https://en.wikipedia.org/wiki/Kaprekar_number
#https://tr.wikipedia.org/wiki/Kaprekar_say%C4%B1lar%C4%B1

#1, 9, 45, 55, 99, 297, 703, 999
for x in xrange(1, 1000):
	if len(str(x**2)) % 2 == 0:
		cache = x ** 2
		if int(str(cache)[-len(str(x)):]) + int(str(cache)[:len(str(x))]) == x:
			print x
