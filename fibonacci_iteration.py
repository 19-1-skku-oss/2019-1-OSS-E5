
## non recursive fibonacci_iteration function.

def fibonacci_iteration(n):
	b = True
	f1 =1
	f2 =1
	
	while n>2:
		if b:
			f1 = f1+ f2
		else:
			f2 = f1+f2

		b = not b
		n = n -1	

	if b:
		reuturn f2
	else:
		return f1		
