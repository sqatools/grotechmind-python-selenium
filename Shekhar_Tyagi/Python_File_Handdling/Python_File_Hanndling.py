def read_file(test_file):
	obj1 = open(test_file,'r')
	data = obj1.read()
	print(data)