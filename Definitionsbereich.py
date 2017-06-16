def f():
	def local():
		var="local"
	def dononlocal():
		nonlocal var
		var ="nonlocal"
	def doglobal():
		global var
		var = "global"
	var="test"
	local()
	dononlocal()
	doglobal()
	print("after init", var)
if __name__ == "__main__":
	f()
	print("global",var)