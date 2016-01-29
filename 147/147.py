#Coded By B3mB4m
#0 < const < 1   
#const = '0,abcdefg' 
#g = {1,3,7,9} 
#And we want 10 pseudorandom .. 

const = 0.3781467 
for x in xrange(0, 10):
	getvalue = const * 147
	print int(getvalue//1)
	const = float("0."+str(getvalue).split(".")[1])
