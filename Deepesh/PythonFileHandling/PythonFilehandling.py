"""
file opening mode
read mode (r)
write mode (w)
apend mode (a)
"""

def read_file(filename):
    obj1 = open(filename, 'r')
    data = obj1.read()
    print(data)
    obj1.close()


# read_file("test_file.txt")
# read_file(r"E:\Filesdata\count_name.txt")
# read_file("E:\\Filesdata\\count_name.txt")



# Write content to the file
# 1. If the target file is already available, then write mode overwrite the existing data
# and add new data.
# 2. if target file is not available then it will create new file
#  with the name provided and add data to the file.

def write_content_to_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()

def read_file_return(filename):
    obj1 = open(filename, 'r')
    data = obj1.read()
    obj1.close()
    return data
# case 1: if file is already available
# write_content_to_file("test_file2.txt", "Hello Good Morning")
# case 2: if file is not available
# write_content_to_file("shekhar_file.txt", "Hello Good Morning")
var1 = """
We are learning Python Programming 
which is very easy to learn and we make 
our career in IT
"""

#write_content_to_file("shekhar_file.txt", var1)

file_data = read_file_return("test_file.txt")
updated_data = file_data.replace('django', 'JAVA')
write_content_to_file("shekhar_file.txt", updated_data)


# Write content to the file with append mode
# 1. if file is already available , then it will add content at end of file
# 2. if file is not available, then it will create new file and add content to the file.

def append_content_file(filename, content):
    file = open(filename, "a")
    file.write(content)
    file.close()

append_content_file("test_file.txt", "Grotech Mind Learning")
append_content_file("test_file5.txt", "Growtech Mind Learning")