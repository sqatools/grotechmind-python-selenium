"""
file opening mode
read mode (r)
write mode (w)
apend mode (a)
"""

# def read_file(filename):
#     obj1 = open(filename, 'r')
#     data = obj1.read()
#     print(data)
#     obj1.close()
#
#
# # read_file("test_file.txt")
# # read_file(r"E:\Filesdata\count_name.txt")
# # read_file("E:\\Filesdata\\count_name.txt")
#
#
#
# # Write content to the file
# # 1. If the target file is already available, then write mode overwrite the existing data
# # and add new data.
# # 2. if target file is not available then it will create new file
# #  with the name provided and add data to the file.
#
# def write_content_to_file(filename, content):
#     file = open(filename, "w")
#     file.write(content)
#     file.close()
#
# def read_file_return(filename):
#     obj1 = open(filename, 'r')
#     data = obj1.read()
#     obj1.close()
#     return data
# # case 1: if file is already available
# # write_content_to_file("test_file2.txt", "Hello Good Morning")
# # case 2: if file is not available
# # write_content_to_file("shekhar_file.txt", "Hello Good Morning")
# var1 = """
# We are learning Python Programming
# which is very easy to learn and we make
# our career in IT
# """
#
# #write_content_to_file("shekhar_file.txt", var1)
#
# file_data = read_file_return("test_file.txt")
# updated_data = file_data.replace('django', 'JAVA')
# write_content_to_file("shekhar_file.txt", updated_data)
#
#
# # Write content to the file with append mode
# # 1. if file is already available , then it will add content at end of file
# # 2. if file is not available, then it will create new file and add content to the file.
#
# def append_content_file(filename, content):
#     file = open(filename, "a")
#     file.write(content)
#     file.close()
#
# append_content_file("test_file.txt", "Grotech Mind Learning")
# append_content_file("test_file5.txt", "Growtech Mind Learning")
#
#
# #  context manager
# def read_file_data(filename):
#     with open(filename) as file1:
#         data = file1.read()
#         print(data)
#         print("close status :", file1.closed)
#         print("filename :", file1.name)
#         print("filemode :", file1.mode)
#
#     print("close status :", file1.closed)


#read_file_data("read_file.txt")

# read file content
# -> read specific number of characters/bytes
# -> Read specific number of lines
# -> Read all the lines in the list

# # -> read specific number of characters/bytes
# def read_specific_char(filename, char_count):
#      with open(filename, 'r') as file:
#          data = file.read(char_count)
#          print(data)

# read_specific_char("read_file.txt", 20)
# Python offers many c

# -> Read specific number of lines with readline method.
# def read_specific_lines(filename,line_num):
#     with open(filename, "r") as file:
#         for i in range(line_num):
#             data1 = file.readline()
#             print(data1, end="")
#
# read_specific_lines("read_file.txt", 5)


# read list of lines with  help of readlines

def read_lines_list(filename, line_number):
    with open(filename, "r") as file:
        if line_number > 0:
            line_number = line_number -1
        lines_list = file.readlines()
        #print(lines_list)
        print(lines_list[line_number])


read_lines_list("read_file.txt", 0)
#read_lines_list("read_file.txt", -2)


# def read_lines_list_specific_range(filename, start, end):
#     with open(filename, "r") as file:
#         lines_list = file.readlines()
#         #print(lines_list[start-1:end])
#         for i in range(start-1, end):
#             print(lines_list[i], end="")


#read_lines_list_specific_range("read_file.txt", 2, 5)


# tell method and seek method

# tell method : this method provides current position of the curser
# seek method : this method helps to move cursor position

# def read_file_with_tell(filename):
#     with open(filename, 'r') as file:
#         print("initial cursor position:", file.tell())
#         data = file.read(10)
#         print("10 byte data :", data)
#         print("cursor position:", file.tell())
#         data20 = file.read(20)
#         print("20 byte data :", data20)
#         print("cursor position:", file.tell())
#
# # read_file_with_tell('read_file.txt')
#
# def read_file_with_seek(filename):
#     with open(filename, "rb") as file:
#         print("initial cursor position:", file.tell())
#         file.seek(20, 0) # start from begining of the file
#         print("cursor position:", file.tell())
#         file.seek(20, 1) # start from current position of the cursor
#         print("cursor position:", file.tell())
#         data = file.read(10)
#         print("data :", data)
#         print("cursor position:", file.tell())
#         file.seek(-50, 2) # set the cursor from end of the file.
#         data = file.read()
#         print("last content of file:", data)
#         print("cursor position:", file.tell())
#
#
# read_file_with_seek("read_file.txt")

























