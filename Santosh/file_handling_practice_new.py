# A=open("first txt file.txt","r")
# B=A.read()
# print(B)
# print("*"*50)
# def file_reading(file_name):
#      A=open("first txt file.txt","r")
#      B=A.read()
#      print(B)
#
# file="first txt file.txt"
# file_reading(file)
#
# print("*"*50)
# def file_reading(file_name):
#      A=open("first txt file.txt","r")
#      B=A.read()
#      print(B)
#file_reading("first txt file.txt")

# print("*"*50)
# file=open("first txt file.txt","w")
# data=file.write("datatype.txt")
# file.close()
# print(data)


# def file_append(filexxx):
#
#     file=open("first txt file.txt","a")
#     data=file.write(content)
#     file.close()
#     print(data)
#
# content="5.i am sacin pawar"
# file_name="first txt file.txt"
# file_append(file_name)

# def read_file_char(file_name,char_count):
#     with open(file_name,"r") as file:
#         data=file.read(char_count)
#         return data
#
# result=read_file_char("first txt file.txt",30)
# print(result)
# print(result.upper())


# def read_file_lines(file_name,line_number):
#     with open(file_name,"r") as file:
#         for i in range(line_number):
#          data=file.readline()
#          print(data)
#
#
# read_file_lines("first txt file.txt",3)


# def read_file_lines(file_name,line_number):
#     with open(file_name,"r") as file:
#         if line_number > 0:
#             line_number = line_number -1
#         lines_list = file.readlines()
#         print(lines_list[line_number])
#
#
# read_file_lines("first txt file.txt",3)


# def read_file_lines(file_name,line_number):
#     with open(file_name,"r") as file:
#         for i in range(line_number):
#          data=file.readline()
#         print(data)
#
#
# read_file_lines("first txt file.txt",3)


# def read_lines_list_specific_range(filename, s, e):
#     with open(filename, "r") as file:
#         lines_list = file.readlines()
#         for i in range(s-1, e):
#             print(lines_list[i], end="")
#
#
# read_lines_list_specific_range("first txt file.txt", 2, 4)


















