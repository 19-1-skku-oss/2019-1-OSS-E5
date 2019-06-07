## algorithms that check whether the number is prime.
## 소수인지 판별


def primeCheck(number):
    """
    A number is prime if it has exactly two dividers: 1 and itself.수

    소수의 정의 : 1과 자기 자신을 약수로 가지는 
    """
    if number < 2:
        # Negatives, 0 and 1 are not primes
        return False
   
   elif number == 2:
	return True

   if n % 2 == 0:
	return False
    
   for i in range(3, n, 2):
	if n%i == 0:
		return False
	return True


if __name__ == '__main__':
unittest.main()
