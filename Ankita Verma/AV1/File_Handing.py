"""def read_file(filename):
    obj1 = open(filename, 'r')
    data = obj1.read()
    print(data)
    obj1.close()"""


# read_file("test_file.txt")
# read_file(r"E:\Filesdata\count_name.txt")
# read_file("E:\\Filesdata\\count_name.txt")

#File Handling read content of the file
"""def readfile(filename): #function defined with argument
    open_file =open(filename,'r') #open a file in a mode
    data=open_file.read()    #store mode in some object
    print(data)       #print data
    open_file.close() #close data

readfile("test.txt")"""

# Write content to the file

#1 if the target file is already available then  write mode will overwrite the data
#2 If file is not avaliable then it will create a file and write

def write_file(filename, content):
    fileopen=open(filename,'w')
    data1=fileopen.write(content)
var1="Hi this this python trainning class"


write_file("test.txt","Hello are you in ")
write_file("test2.txt","Newly created file")
write_file("test1.txt", var1)
import openpyxl
#File Append Mode
#1.if file is not avaliable then it will add the content end of file
#2.If file does not exist then it will create and add the content

def file_append_mode(filename,content):
    file_open=open(filename,'a')
    file_open.write(content)




file_append_mode("test2.txt","Append Success")
file_append_mode("test3.txt","Append Success in text3 file")



