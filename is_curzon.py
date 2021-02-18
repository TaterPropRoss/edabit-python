def is_curzon(num):
	setNum = 2
	powerNum = 1 + setNum ** num
	multNum = 1 + setNum * num
	remainder = bool(powerNum % multNum) # check if there is a remainder
	return not(remainder)