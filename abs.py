## algorithms that finds the largest the elements in the array

from abs import absVal

def absVal(num):
    ## Ex
    ##>>>absVal([0, 5, 1, 11])
    ## 11
    ##>>>absVal([3, -10, -2])
    ## 3

    temp = absVal(num[0])
    for i in num:
	if absVal(i) > temp: ## if there is elements that is larger than temp,
		temp = i     ## temp is not the largest -> swap
    return temp              ## return the largest elements. 

def main():
    a = [1, 2, 3]
    b = absVal(a)
    print(b)   ##3

if __name__ == '__main__':
	main()
