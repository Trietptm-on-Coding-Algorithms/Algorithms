#https://en.wikipedia.org/wiki/Ones'_complement
#Coded By B3mB4m
#This script just for algorithm and just include hex to one's implement.
#Feel free to edit,use etc.. (any fcking thing)


def oneScomplement( number):
	list = []
	number = number[::-1]
	total = 0
	oneScomplement = ""
	for x in xrange(0, len(str(number))):
		if   str(number[x]).upper() == "A":  total = total + int(10)*(16**x);
		elif str(number[x]).upper() == "B":  total = total + int(11)*(16**x);
		elif str(number[x]).upper() == "C":  total = total + int(12)*(16**x);
		elif str(number[x]).upper() == "D":  total = total + int(13)*(16**x);
		elif str(number[x]).upper() == "E":  total = total + int(14)*(16**x);
		elif str(number[x]).upper() == "F":  total = total + int(15)*(16**x);
		else:	total = total + int(number[x])*(16**x)

	while total >= 1:
		list.append(str(total % 2))
		total = total / 2
	total = str("".join(list[::-1]))

	for x in total:
		if x == "1":
			oneScomplement += "0"
		else:
			oneScomplement += "1"
	return oneScomplement
