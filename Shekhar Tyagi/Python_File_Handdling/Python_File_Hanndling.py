def read_file(test_file):
	obj1 = open(test_file,'r')
	data = obj1.read()
	print(data)

# read_file("test_file.txt")
# read_file("D:\\test_File.txt")

def write_content_to_the_file(filename , content):
	file = open(filename,'w')
	file.write(content)
	file.close()
write_content_to_the_file("shekhar_file.txt" , " Hello Brother")

def append_content_to_the_file(filename , content):
	file = open(filename,'a')
	file.write(content)
	file.close()
append_content_to_the_file("write_file.txt" ," Hello , Good Morning brother")
