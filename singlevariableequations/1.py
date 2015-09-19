import re

#Coded By B3mB4m
#(7x-4)=(5x-8) 


orjinalequation = raw_input("\nProblem : ")
equation = orjinalequation.split("=")
print ""

proceslist = ["+","-","*","/"]
for x in xrange(0,len(equation)):
	catchorder = x
	if "(" or ")" in equation[x]:
		find = re.findall("(\S+)", equation[x])
		if len(find) > 2:
			print "Brain Error"
		else:	
			find[0] = find[0].replace(")", "").replace("(", "")
			for x in proceslist:
				if x in find[0]:
					if "x" in find[0]:
						locationX = proceslist[proceslist.index(x)]
						find[0] = find[0].split(locationX) 
						whereX = [x for x in find[0] if "x" in x]
						if len(whereX) == 1:
							if catchorder == 0:
								_unkown = find[0][find[0].index(whereX[0])]
								_number = int(find[0][1])
							else:	
								_unkown2 = find[0][find[0].index(whereX[0])]
								_number2 = int(find[0][1])	
							if locationX == "-":
								try:
									_number = -_number 
									_number2 = -_number2
								except:
									pass	

if int(re.sub("x","",_unkown)) > int(re.sub("x","",_unkown2)):
	unkownresult = "%d-%d" % (int(re.sub("x","",_unkown2)),int(re.sub("x","",_unkown)))
else:
	unkownresult = "%d-%d" % (int(re.sub("x","",_unkown)),int(re.sub("x","",_unkown2)))
numberresult = "%d-%d" % (_number,_number2)

print  "X = %.2f" % (int(eval(numberresult)) / int(eval(unkownresult)))
