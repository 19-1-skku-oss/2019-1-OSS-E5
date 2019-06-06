'''
Numerical integration or quadrature for a smooth function f with known values at x_i
This method is the classical approch of suming 'Equally Spaced Abscissas' 
method 2: 
"Simpson Rule"
'''


'''
What's is the simson rules?
곡선 하부의 면적을 구할 때 쓰임.
n개의 등간격 종선으로 나누어(n+1개의 종선이 있는 경우) n개의 구간을 2개씩 
묶은 것을 면적요소로 생각하여 전체는 1/2n개의 면적요소로 보는 것.


'''
from __future__ import print_function


def method_2(boundary, steps):
# "Simpson Rule"
# int(f) = delta_x/2 * (b-a)/3*(f1 + 4f2 + 2f_3 + ... + fn)
	
	h = (boundary[1] - boundary[0]) / steps (한 칸의 크기 설정)
	a = boundary[0]
	b = boundary[1]
	x_i = makePoints(a,b,h)
	y = 0.0
	y += (h/3.0)*f(a)
	cnt = 2
	for i in x_i:
		y += (h/3)*(4-2*(cnt%2))*f(i)	
		cnt += 1
	y += (h/3.0)*f(b)
	return y

def makePoints(a,b,h):
	x = a + h ##초기값에서 한 간격을 더함.
	while x < (b-h): ## x가 마지막 점에서 한 간격 전 크기의 값이 될 때까지
		yield x
		x = x + h  ## 한 칸씩 늘려준다 -> while문을 빠져나오면 마지막점에서 두 간격 전임 
	return x

def f(x): #enter your function here
	y = (x-0)*(x-0)
	return y

def main():
	a = 0.0 #Lower bound of integration(초기점)
	b = 1.0	#Upper bound of integration(마침점)
	steps = 10.0		#define number of steps or resolution(간격)
	boundary = [a, b]	#define boundary of integration(범위)
	y = method_2(boundary, steps)
	print('y = {0}'.format(y))

if __name__ == '__main__':
main()
