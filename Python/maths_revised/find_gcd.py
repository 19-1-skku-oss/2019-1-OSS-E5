## algorithms that find greatest common multiple
## 최대공약수를 구하는 함수
## 유클리드 호제법 이용!

'''
a mod b = 0 이라면, gcd(a,b) = b
a mod b !=0 이라면, gcd(a,b) = gcd(b, a mod b) 성립!!

'''

def find_gcd(num_1, num_2):
   mod = a%b
   while mod>0:
	num_1 = num_2
	num_2 = mod
	mod = num_1 % num_2
   
   return num_2

def main():
    num_1 = input("Input num_1")
    num_2 = input("Input num_2")
    print(find_lcm(num_1, num_2))


if __name__ == '__main__':
	main()
