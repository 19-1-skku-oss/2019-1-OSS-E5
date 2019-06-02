#recursion function of honoi tower problem

from __future__ import print_function


log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


def Tower_Of_Hanoi(n, source, dest, by, movement):
    if n >= 1:
	Tower_Of_Hanoi(n-1, source, movement, by)
	moveDisk(source, by)
	Tower_Of_Hanoi(n-1, movement, by, source)
## recursive fun

def moveDisk(fp, tp):   ## the function that print the moving situation of the tower.
	print(('Moving disk from', fp, 'to', tp))


def main():
	height = int(input('Height of hanoi: '))
	## user input the number of height of hanoi tower.

	Tower_Of_Hanoi(height, 'A', 'B', 'C')


if __name__ == '__main__':
	main()
