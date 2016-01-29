#https://en.wikipedia.org/wiki/Ones'_complement
#Coded By B3mB4m
#This script just for algorithm and just include hex to one's implement.
#Feel free to edit,use etc.. (any fcking thing)


def oneScomplement( number):
	list = []
	number = str(number).upper()[::-1]
	total = 0
	oneScomplement = ""
	for x in xrange(0, len(number)):
		if   number[x] == "A":  total = total + 10*(16**x);
		elif number[x] == "B":  total = total + 11*(16**x);
		elif number[x] == "C":  total = total + 12*(16**x);
		elif number[x] == "D":  total = total + 13*(16**x);
		elif number[x] == "E":  total = total + 14*(16**x);
		elif number[x] == "F":  total = total + 15*(16**x);
		else:	total = total + int(number[x],10)*(16**x)

	while total >= 1:
		oneScomplement += str(total%2)
		total = total // 2
	return oneScomplement
