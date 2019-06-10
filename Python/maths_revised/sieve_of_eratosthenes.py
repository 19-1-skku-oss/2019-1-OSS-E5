## 소수를 찾는 방법. 고대 그리스 수학자 에라토스테네스가 발견함.

'''
1. 2부터 소수를 구하고자 하는 구간의 모든 수를 사각형으로 나열한다. 
2. 2는 소수이므로 오른쪽에 2를 쓰고 자기 자신을 제외한 모든 2의 배수를 지운다.
3. 남아있는 가운데 3은 소수이므로 오른쪽에 3을 쓴다.
4 .자기 자신을 제외한 3의 배수는 모두 지운다.
5. 남아있는 가운데 5 자기 자신을 제외하고 5의 배수를 모두 지운다.
6. 남아있는 가운데 7은 소수이므로 자기 자신을 제외한 7의 배수는 모두 지운다.
7. 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다. 


Ex) 120까지의 소수를 구하려면, 11^2>120 이므로 11보다 작은 수의 배수들만 지워도 충분하다.
-> 120보다 작거나 같은 수 가운데, 2, 3, 5, 7의 배수를 지우고 남는 수는 모두 소수이다. 

'''

def sieve_of_eratosthenes(n):
	numbers = range(2, n)
	while len(numbers) > 0:
		numbers = [num for num in numbers if num % numbers[0] != 0 or num == numbers[0]]
	yield numbers[0]
	numbers = numbers[1:]

num = input()
print(sieve_of_eratosthenes(num))
