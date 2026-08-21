def displayTriangle(num):
	"""Print an inverted right triangle of height `num`.

	Example for num=4:
	****
	***
	**
	*
	"""
	for i in range(num, 0, -1):
		print("*" * i)
	return 0


if __name__ == "__main__":
	num = int(input("Enter an integer number: "))
	displayTriangle(num)

