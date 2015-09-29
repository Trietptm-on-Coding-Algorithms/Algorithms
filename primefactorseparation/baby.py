number = 141414
mylist = []

#Coded By B3mB4m

for x in xrange(2, 100):
	if len([y for y in range(2,x)  if x%y == 0]) == 0:
		while number > 1:
			if number % x == 0:
				number = number / x
				mylist.append(x)
			else:
				break
print mylist
