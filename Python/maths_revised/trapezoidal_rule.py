'''
Numerical integration or quadrature for a smooth function f with known values at x_i
This method is the classical approch of suming 'Equally Spaced Abscissas' 
method 1: 
"extended trapezoidal rule"

사다리꼴 공식(trapezoidal rule of integration)
f(x)의 적분을 사다리꼴 넓이로 근사시키는 방법
-> 가장 단순하지만 오차가 크긴 함.

넓이 S = 1/2*(f[a] + f[b]) *(b-a)

f(x) 적분은 약 (b-a)(f[a] + f[b]) / 2 에 수렴
-> 죽, 함수값의 평균값

'''
from __future__ import print_function

def method_1(boundary, steps):
# "extended trapezoidal rule"
# int(f) = dx/2 * (f1 + 2f2 + ... + fn)
	h = (boundary[1] - boundary[0]) / steps  ##한 칸의 간격을 구하는 부분
	a = boundary[0] ##시작점
	b = boundary[1]  ## 도착점
	x_i = makePoints(a,b,h)
	y = 0.0	
	y += (h/2.0)*f(a)
	for i in x_i:
		#print(i)	
		y += h*f(i)
	y += (h/2.0)*f(b)	
	return y	

def makePoints(a,b,h):
	x = a + h	
	while x < (b-h):
		yield x
		x = x + h  ##return b - 2*h
		
def f(x): #enter your function here
	y = (x-0)*(x-0)
	return y

def main():
	a = 0.0 #Lower bound of integration
	b = 1.0	#Upper bound of integration
	steps = 10.0		#define number of steps or resolution	
	boundary = [a, b]	#define boundary of integration
	y = method_1(boundary, steps)
	print('y = {0}'.format(y))

if __name__ == '__main__':
main()
