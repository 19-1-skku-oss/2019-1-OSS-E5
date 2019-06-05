
# Greater Common Divisor - https://en.wikipedia.org/wiki/Greatest_common_divisor
##			   Euclid methods			

def gcd(a, b):
	if (a==0):
		return b
	else:
		result = gcd(b%a, a)
		return result

def main():
    
    try:
        nums = input("Enter two Integers separated by comma (,): ").split(',')
        num1 = int(nums[0])
	num2 = int(nums[1])

    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong Input")
    print("gcd({num1}, {num2}) = {gcd(num1, num2)}")

if __name__ == '__main__':
	main()


## fix spelling error(f), python grammar(unneeded ;)
