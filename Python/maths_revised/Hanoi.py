#recursion function of honoi tower problem

from __future__ import print_function


log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


def Tower_Of_Hanoi(n, source, aux, destination):   
    if n >= 1:
	Tower_Of_Hanoi(n-1, source, destination, aux)
	moveDisk(source, by)
	Tower_Of_Hanoi(n-1, destination, aux, source)

## recursive func

def moveDisk(fp, tp):   ## the function that print the moving situation of the tower.
	print(('Moving disk from', fp, 'to', tp))


def main():
	height = int(input('Height of hanoi: '))
	## user input the number of height of hanoi tower.
        ## the number of total disks 

	Tower_Of_Hanoi(height, 'A', 'B', 'C')   
        ## there are 3 tower named A, B, C, and disks (the number of height)


if __name__ == '__main__':
	main()
