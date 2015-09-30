#Coded By B3mB4m
#Amicable Numbers
#https://en.wikipedia.org/wiki/Amicable_numbers
#https://tr.wikipedia.org/wiki/Arkada%C5%9F_say%C4%B1lar


firstnumber  = input("First number :")
secondnumber = input("Second number :")
cache1 =  [x for x in xrange(1, firstnumber) if firstnumber % x == 0]
cache2 =  [x for x in xrange(1, secondnumber) if secondnumber % x == 0]

if sum(cache1) == secondnumber and sum(cache2) == firstnumber:
	print "That numbers %d&%d are friend ! xD" % (firstnumber, secondnumber)
