#the algorithms that return the average value of total elements.

def average(array):
    sum = 0
    for x in array:
      sum += x
    avg = sum / len(array)
    return avg

def main():
  print(average([2, 4, 6, 8, 20, 50, 70]))

if __name__ == '__main__':
main()
