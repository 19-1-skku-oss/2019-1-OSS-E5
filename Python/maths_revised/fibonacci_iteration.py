## non recursive fibonacci_iteration function.

def fibonacci_iteration(n):
	status = True
	f1 =1  ## 1번째 인자
	f2 =1 ## 2번째 인자
	
	## -> 각 단계의 피보나치 수를 저장할 두 개의 변수


	while n>2:  ## 정지 조건이 2가 되는 것은 이미 f1, f2에 2개의 피보나치 수를 가지고 시작하기 때문임.
		if status:   ## 현재 상태를 파악하고 피보나치 수를 구해나가는 부분.
			f1 = f1+ f2
		else:
			f2 = f1+f2

		stats = not status
		n = n -1	

	if status:
		reuturn f2
	else:
		return f1		
