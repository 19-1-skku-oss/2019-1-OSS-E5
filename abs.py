def absVal(num):
    """
    Function to fins absolute value of numbers.
    >>absVal(-5)
    5
    >>absVal(0)
    0
    """
    if num < 0:     ## if num is negative elements, change to positive value.
        return -num
    else:  	    ## we don't need any other things if num is positive value
        return num  ## because if the elements is positive, abs and origin value is same.

def main():
    print(absVal(-34)) # = 34

if __name__ == '__main__':
main()
