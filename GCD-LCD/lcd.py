#Coded By B3mB4m
#LCD - Least Common Multiple

a = 6
b = 8

cachea = [x*a  for x in xrange(1, 40)]
cacheb = [x*b for x in xrange(1, 40)]

for x in xrange(1, 40):
	for y in xrange(1, len(cachea)):
		if cachea[y] in cacheb:
			print "%d & %d LCD : %d" % (a,b,cachea[y])
			break
	break
