number = raw_input("Number : ")
#Coded By B3mB4m
print eval("*".join([str(x) for x in xrange(1,int(number)+1)][::-1]))

