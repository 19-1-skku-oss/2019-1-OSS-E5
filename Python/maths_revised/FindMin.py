# Find the smallest value in the array.

def findMin(x):
    minNum = x[0] # Comparison from the first element to the last element.

    for i in x:
        if minNum > i:  # if min is larger than nums[x], then change min to num[x]
		minNum = i

	return minNum

def main():
    print(findMin([0,1,2,3,4,5,-3,24,-56])) # = -56

if __name__ == '__main__':
    main()
