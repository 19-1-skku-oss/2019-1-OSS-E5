##algorithms that find least common multiple
## 최소공배수를 구하는 함수
## 유클리드 호제법 이용하기!

import find_gcd

def find_lcm(num_1, num_2):
    return num_1 * num_2 // find_gcd(num_1, num_2)

def main():
    num_1 = input("Input num_1")
    num_2 = input("Input num_2")
    print(find_lcm(num_1, num_2))


if __name__ == '__main__':
	main()
