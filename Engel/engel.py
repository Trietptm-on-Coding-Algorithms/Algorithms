#Coded By B3mB4m

#0 <= n <= 1
#u(n) = s
#u(n)+1 = {(u(n)+PI)**8}
#Assume S 0.27348
#And we want 10 random ..

const = 0
pi = 3.14159
for x in xrange(0, 10):
	cache = (const+pi)**8 
	print str(cache).split(".")[1]
	const = float("0."+str(cache).split(".")[1])
