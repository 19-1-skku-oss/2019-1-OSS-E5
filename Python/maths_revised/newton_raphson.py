'''
    Author: P Shreyas Shetty
    Implementation of Newton-Raphson method for solving equations of kind
    f(x) = 0. It is an iterative method where solution is found by the expression
        x[n+1] = x[n] + f(x[n])/f'(x[n])
    If no solution exists, then either the solution will not be found when iteration
    limit is reached or the gradient f'(x[n]) approaches zero. In both cases, exception
    is raised. If iteration limit is reached, try increasing maxiter.
	
   Newton-Raphson methods는 방정식의 근을 구하는 알고리즘이다.
   초기값을 입력하면 입력값에 해당하는 방정식의 값에서의 접선의 방정식을 구하고, 그 방정식의
   근을 또다시 초기값으로 갱신한다.
   즉, 
   1. 초기값을 입력한다.
   2. 초기값을 x로 하여 f(x)를 구한ㄷ.ㅏ
   3. f(x)에서의 접선의 방정식을 구한다.
   4. 구해진 접선의 방정식의 근 x'를 구한다.
   5. 구해진 근의 f(x)'가 0이 되는지를 판별한다. + 0에 수렴하는지
   6. x가 오차범위 이내가 아니라면 x'를 x로 갱신한다. 
   7. 2~6번 과정을 반복한다. 
    
'''

import math as m

def calc_derivative(f, a, h):
    '''
     Calculates derivative at point a for function f using finite difference
     method
    '''
    h = 0.000001
    derivative = (f(x+h) - f(x)) / h
    return drivative

def f(x):
	function = (x*x*X) - (2*x) - 1
	return function

def newton_raphson(x):
	newton = x - (f(x)/calc_derivative(x))


def newton_raphson(p, n):
    
##p = 초기값(접선으로 그을 때 가장 처음이 되는 첫번째 점)
##n = iterations의 수 (반복 과정의 수)

    a = x0 #set the initial guess
    for i in range(n):
        if i == 0:  ## 처음 근사값을 계산. 
            x = newton_raphson(p)
	else:
		x = newton+raphson(terate(x,n))
	
return x
 
if __name__ == '__main__':
print iterate(1,3)  ## 여기서 함수 f(x) = x^3 - 2x -1
