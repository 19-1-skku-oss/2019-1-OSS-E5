'''
Numerical integration or quadrature for a smooth function f with known values at x_i
This method is the classical approch of suming 'Equally Spaced Abscissas' 
method 2: 
"Simpson Rule"
'''


'''
What's is the simson rules?
방정식 P(x) 라는 이차방정식이 있으면, f(x)의 근사값을 구한다.
여기서 P(x)는 P(x) 위에 있는 임의의 a, b, 그리고 그 둘의 중간값 m = (a+b)/2 을 구하고
중간값의 f(x)와 같은 값을 갖는 근사식이다. 

P(x) 식을 전개하면서 다음 심프신 공식을 구한다. 
https://ko.wijipedia.org/wiki/심프신_공식 참고

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
	x = a + h
	while x < (b-h):
		yield x
		x = x + h  ##update

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
