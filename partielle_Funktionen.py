from functools import partial
def mal(x, y):
	return x * y

mal2 = partial(mal, 2, 10)
print(mal2())