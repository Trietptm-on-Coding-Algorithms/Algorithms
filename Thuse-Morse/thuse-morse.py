import random
#Coded By B3mB4m
#Thue-Morse Sequence
#1 -> 10
#0 -> 01

numbercache = ""
number = 10
stop = 6 #Just 6 times 
while stop > 0:
	for x in [x for x in str(number)]:
		if int(x) == 1:
			numbercache += "10"
		else:
			numbercache += "01"
		number = int(numbercache)
	stop = stop - 1
	print numbercache 
