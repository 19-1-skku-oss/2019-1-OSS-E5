## algorithms that check whether the number is prime.
## 소수인지 판별


import math
import unittest


def primeCheck(number):
    """수
    A number is prime if it has exactly two dividers: 1 and itself.

    소수의 정의 : 1과 자기 자신을 약수로 가지는 
    """
    if number < 2:
        # Negatives, 0 and 1 are not primes
        return False
    if number < 4:
        # 2 and 3 are primes
        return True
    if number % 2 == 0:
        # Even values are not primes
        return False

    # Except 2, all primes are odd. If any odd value divide
    # the number, then that number is not prime.
    # 3이하의 짝수인 소수는 2일 뿐 -> 그 외 모든 짝수는 소수가 아니다!

    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2)
    return not any(number % i == 0 for i in odd_numbers)


class Test(unittest.TestCase):
    def test_not_primes(self):
        self.assertFalse(primeCheck(-19),
                "Negative numbers are not prime.")
        self.assertFalse(primeCheck(0),
                "Zero doesn't have any divider, primes must have two")
        self.assertFalse(primeCheck(1),
                "One just have 1 divider, primes must have two.")
        self.assertFalse(primeCheck(2 * 2))
        self.assertFalse(primeCheck(2 * 3))
        self.assertFalse(primeCheck(3 * 3))
        self.assertFalse(primeCheck(3 * 5))
        self.assertFalse(primeCheck(3 * 5 * 7))


if __name__ == '__main__':
unittest.main()
