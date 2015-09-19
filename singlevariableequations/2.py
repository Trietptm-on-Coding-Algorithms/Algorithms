import re
import sys

#Coded By B3mB4m


problem = "15x+10=25"
problem = problem.split("=")

whereis = [x for x in "+","-","*","/" if x in problem[0]]
whereis2 = [x for x in "+","-","*","/" if x in problem[1]]
cache = "1"
for number in xrange(0, 99999):
	test = re.sub("x","*"+str(number)+".",problem[0])
	test1 = re.sub("x","*"+str(number)+".",problem[1])
	if eval(test) == eval(test1):
		cache = "2"
		print "X = %s" % number
		sys.exit()
if cache == "1":
	for number in xrange(-99999, 0):
		test = re.sub("x","*"+str(number),problem[0])
		test1 = re.sub("x","*"+str(number),problem[1])
		if eval(test) == eval(test1):
			cache = "Find"
			print "X = %s" % number
			sys.exit()
