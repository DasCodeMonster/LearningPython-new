f = lambda x : x%2==0

# def f2(x, y):
	# return x*y
# print(f2(4,2))
liste = [4,2,5,6,3]
liste2 = list(filter(f, liste))
print(liste2)
