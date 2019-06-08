# Fibonacci Sequence Using Recursion

def recur_fibo(n):
    if n <= 1:   ## 받은 n이 음수이거나, 1일 때 그대로 n을 return
        return n
    else:
        (recur_fibo(n-1) + recur_fibo(n-2))  ## 피노나치 수열 : n3 = n1 = n2

def isPositiveInteger(limit):
    if limit >= 0:
	return TRUE
    else:
	return FALSE

def main():
    limit = int(input("How many terms to include in fibonacci series: "))
    if isPositiveInteger(limit):
        print("The first {limit} terms of the fibonacci series are as follows:")
        print([recur_fibo(n) for n in range(limit)])
    else:
        print("Please enter a positive integer: ")

if __name__ == '__main__':
	main()
