#Coded By B3mB4m
#GCD - Greatest common divisor

a = 396 
b = 120

if a > b: 
	x = a
else: 
	x = b

while x > 0:
	if a%x == 0 and b%x == 0:
		print "%d & %d GCD : %d" % (a,b,x)
		break
	x = x - 1 
