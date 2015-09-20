#Coded By B3mB4m
#https://en.wikipedia.org/wiki/Middle-square_method

random = []
const = "32563247"
for x in xrange(0, 11):
	r = len(const) / 4 
	if len(const[:r]) != 2:
		random.append(const[:r+1])
	else:
		random.append(const[:r])
	mutliple = int(const[r:-r]) **2
	const = str(mutliple)
print random[1:]
