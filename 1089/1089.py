#Coded By B3mB4m
#1089 Numbers
#Number digits must be different ..

number1 = 836
number2 = int(str(number1)[::-1])

if number1 > number2:
	cache = number1 - number2 
else:
	cache = number2 - number1

print cache+int(str(cache)[::-1])
