## algorithms that find greatest common multiple
## 최대공약수를 구하는 함수
'''
a mod b = 0 이라면, gcd(a,b) = b
a mod b !=0 이라면, gcd(a,b) = gcd(b, a mod b) 성립!!

'''

def find_gcd(num_1, num_2):
    if num_1 < num_2:
	(num_1, num_2) = (num_2, num_1)  ## swap num_1 & num_2
    while num_2 != 0:
	(num_1, num_2) = (num_2, num_1 % num_2)

    return num_1

def main():
    num_1 = input("Input num_1")
    num_2 = input("Input num_2")
    print(find_lcm(num_1, num_2))


if __name__ == '__main__':
	main()
