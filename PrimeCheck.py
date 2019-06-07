## algorithms that check whether the number is prime.
## 소수인지 판별


import math
import unittest


def primeCheck(number):
    """
    A number is prime if it has exactly two dividers: 1 and itself.수

    소수의 정의 : 1과 자기 자신을 약수로 가지는 수
	만약 N = a* b 라면, N은 a, b 모두 다 나누어진다.
	-> N의 제곱근 r을 기준으로 곱해서 N이 될 수 있는 약수들이 같은 개수로 분포한다.
	=> 따라서 N이 소수인지를 알고 싶으면 N의 제곱근까지만 검사하면 된다!
    """
    if number < 2:
        # Negatives, 0 and 1 are not primes
        return False
   
   if n == 2:
	return True

   if n % 2 == 0:
	return False
    
   l = math.sqrt(n)

   for i in range(3,l,2):
	if n%i == 0:
		return False


    return True


if __name__ == '__main__':
unittest.main()
