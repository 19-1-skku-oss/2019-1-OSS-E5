##algorithms that find least common multiple
## 최소공배수를 구하는 함수

def find_lcm(num_1, num_2):
    if(num_1 > num_2)
	max = num_1
    else:
	max = num_2
    lcm = max
   
    while (True):
        if ((lcm % num_1 == 0) and (lcm % num_2 == 0)):
            break
        lcm += max
    return lcm


def main():
    num_1 = input("Input num_1")
    num_2 = input("Input num_2")
    print(find_lcm(num_1, num_2))


if __name__ == '__main__':
	main()
