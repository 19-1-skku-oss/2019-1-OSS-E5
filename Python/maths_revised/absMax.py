## algorithms that finds the largest absVal elements in the array

from abs import absVal

def absMax(num):
    ## Ex
    ##>>>absVal([0, 5, 1, 11])
    ## 11
    ##>>>absVal([3, -10, -2])
    ## -10

    temp = absVal(num[0])
    for i in num:
	if absVal(i) > temp: ## if there is elements that is larger than abs temp,
		temp = i     ## temp is not the largest -> swap
    return temp              ## return the largest elements. 

## the value is absVal types(absVal func)

def main():
    a = [1, 2, -3]
    b = absMax(a)
    print(b)   ##3

if __name__ == '__main__':
	main()
