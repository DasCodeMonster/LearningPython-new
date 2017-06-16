#Fib
def fib(n):
	if n<2:
		return n
	else:
		return fib(n-1)+fib(n-2)
f=fib(10)
print(f)