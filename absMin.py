from Maths.abs import absVal

#절댓값 값이 가장 작은 것을 고르시오.

def absMin(x):
    """
    # >>>absMin([0,5,1,11])
    0
    # >>absMin([3,-10,-2])
    -2
    """
    temp = x[0]
    for i in x:
        if absVal(i) < absVal(temp):
            temp = i
    return temp

def main():
    a = [-3,-1,2,-11]
    b = absMin(a)
    print(b)  # = -1

if __name__ == '__main__':
	main()
