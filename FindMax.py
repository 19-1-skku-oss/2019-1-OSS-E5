# Find the largest value in the array.

def find_max(nums):
    max = nums[0] # Comparison from the first element to the last element. 
    for x in nums:
      if x > max:  # if max is smaller than nums[x], then change max to num[x]
        max = x

    return(max)

def main():
  a = find_max([2, 4, 9, 7, 19, 94, 5])  
 # max = 94
  print(a)

if __name__ == '__main__':
main()
