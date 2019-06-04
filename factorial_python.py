# Python program that find the factorial of a number provided by the user.

def factorial_python():

	factorial = 1
	# check if the number is negative, positive or zero
	if num < 0:
	   print("Sorry, factorial does not exist for negative numbers")
	elif num == 0:
	   print("The factorial of 0 is 1")
	else:
	   for i in range(1,num + 1):
	       factorial = factorial*i
	   return factorial

if __name__ == '__main__':
	num = int(input("Input your number"))  ##User input his own num.
	print("The factorial of",num,"is",factorial_python(num))
