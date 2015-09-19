#F0 = 0,#F1 = 1
#Fn = Fn-1 + Fn-2   
#Coded By B3mB4m

f0=0;f1=1;f2=0;x=0
while (x<11):
	f2 = f0+f1
	f1 = f0	  
	f0 = f2	  
	x = x+1
	print f2
