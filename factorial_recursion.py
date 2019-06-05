#recursion version of factorial_function.

def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)


if __name__ == '__main__'
	num = int(input("INPUT"))
	print(factorial(num))

