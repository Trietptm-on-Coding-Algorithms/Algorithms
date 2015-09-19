import re
import sys

#Coded By B3mB4m

class B3mB4m(object):
	def __init__(self):
		self.left = []
		self.right = []
		self.answer = "String"
		self.wichone = ""

	def calculate(self, equation):	
		orjinalequation = equation
		self.equation = orjinalequation.split("=")

		for x in xrange(0,len(self.equation)):
			if "("  in self.equation[x] or ")"  in self.equation[x]:
				find = re.findall("(\S+)", self.equation[x])
				if len(find) > 2 or len(find) < 1:
					print "Brain Error"
				else:	
					if x == 0:
						self.left.append(find[0].replace(")", "").replace("(", ""))
					else:
						self.right.append(find[0].replace(")", "").replace("(", ""))
			else:
				self.equation[x] = re.findall("(\S+)", self.equation[x])
				if len(self.equation[x]) > 2 or len(self.equation[x]) < 1:
					print "Brain Error"


		if "(" in orjinalequation:
			self.bruteforce( self.left[0], self.right[0])
			
		else:	
			self.bruteforce( self.equation[0][0], self.equation[1][0])


		if isinstance(self.answer, int):
			print "X = %d" % self.answer
		else:
			if self.wichone == "lef&right":
				self.bruteforce( self.left[0], self.right[0], True)
			else:
				self.bruteforce( self.equation[0][0], self.equation[1][0], True)

				
	def	bruteforce(self, left ,right, fractions=False):
		if fractions == False:
			for number in xrange(-1, 9999):
				test = re.sub("x","*"+str(number)+".0",left)
				test1 = re.sub("x","*"+str(number)+".0",right)
				if eval(test) == eval(test1):
					self.answer = number
					self.wichone = "lef&right"
					return True

			for number in xrange(-9999, 0):
				test = re.sub("x","*"+str(number)+".0",left)
				test1 = re.sub("x","*"+str(number)+".0",right)
				if eval(test) == eval(test1):
					self.answer = number
					return True

		else: 
			leftX = re.search("-?[0-9]*x", left).group()
			leftInt = int(re.search("-?[0-9]*$", left).group())
			rightX = re.search("-?[0-9]*x", right).group()
			rightInt = int(re.search("-?[0-9]*$", right).group())


			if int(leftX.split("x")[0]) > int(rightX.split("x")[0]):
				totalX = int(re.sub("x","",leftX)) - int(re.sub("x","",rightX))
				totalInt = rightInt + (leftInt*(-1))
				frac = "%s/%s" % (str(totalInt), str(totalX))
				print "X = %s" % frac
				sys.exit()
			else:
				totalX = int(re.sub("x","",rightX)) - int(re.sub("x","",leftX))
				totalInt = leftInt + (rightInt*(-1))
				frac = "%s/%s" % (str(totalInt), str(totalX))
				print "X = %s" % frac
				sys.exit()
	

B3mB4m().calculate( "7x-4=5x-8")
