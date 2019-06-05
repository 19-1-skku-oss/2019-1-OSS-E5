## implementation modular exponentation
## Calculating value of base^power % mod


def modularExponential(base, power, mod):
	if power < 0:
		return -1
	base %= mod
	result = 1

	while power > 0:
		if power & 1:
			result = (result * base) % mod
		power = power >> 1
		base = (base * base) % mod
	return result


def main():
	## user input number of base, power, mode. 

	base = int(input("INPUT BASE: "))
	power = int(input("INPUT POWER: "))
	mode = int(input("INPUT MOD: "))	

	print(modularExponential(base, power, mod))


if __name__ == '__main__':
main()
