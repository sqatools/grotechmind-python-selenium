# 1). Python Program How to read a file in reading mode.
"""
def read_file(file_name):
    file=open('LCM.txt','r')
    data=file.read()
    print(data)
read_file('LCM.txt')
"""



"""
def read_file(file_name):
    obj=open('LCM.txt','r')
    data=obj.read()
    print(data)
    obj.close()
#read_file('LCM.txt')

# 2). Python file program to overwrite the existing file content.
def overwrite(file_name,content):
    obj=open('LCM.txt','w')
    data=obj.write(content)
    print(data)
    obj.close()
"""
#overwrite('LCM.txt','hi good morning its overwrite in existing file')
"""
def overwrite_existing_file(file_name,content):
    var1=open('LCM.txt','w')
    var2=var1.write(content)
    print(var2)
    var1.close()
overwrite_existing_file('LCM.txt','Hi im practicing on file handling in that im overwritin data in existing file')
"""

# 3). Python file program to append data to an existing file.
"""
def append_data_in_existing_file(file_name,content):
    var1=open("LCM.txt",'a')
    var2=var1.write(content)
    print(var2)
    var1.close()
append_data_in_existing_file('LCM.txt','here im appending data in existing file using file handling in '
                                       'that im first opening file into append mode')
"""


# 4). Python file program to get the file’s first three and last three lines.
"""
var1=open('LCM.txt','r')
var3=var1.readlines()

for i in (var3[:3]):
    print(i)
for i in (var3[:3]):
    print(i)
"""
"""
var1=open('LCM.txt','r')
var2=var1.readlines()

for i in (var2[:3]):
    print(i)
for i in (var2[:3]):
    print(i)
"""


# 5). Python file program to get all the email ids from a text file.

"""
email_list=[]
var1=open('emp.txt','r')
var2=var1.read()
word_list=var2.split()

for word in word_list:
    if '@' in word:
        email_list.append(word)
    else:
        continue
print(email_list)

"""
"""
email_lst=[]
var1=open('emp.txt','r')
var2=var1.read()
word_lst=var2.split()

for word in word_lst:
    if '@' in word:
        email_lst.append(word)
    else:
        continue
print(email_lst)

"""

# 6). Python file program to get a specific line from the file.

"""
var1=open('emp.txt','r')
var2=var1.readlines()

print(var2[4])
"""

# 7). Python file program to get odd lines from files and append them to separate files.
"""
f1=open('emp.txt','r')
var2=f1.readlines() #Return all lines in the file, as a list where each line is an item in the list object:
f3=open('odd.txt','w')
for i in range(0,len(var2)):
    if i%2!=0:
        f3.write(var2[i])
    else:
        pass
f1.close()
f3.close()
"""

"""
f1=open('emp.txt','r')
var2=f1.readlines()
print(var2)
for i in range (0,len(var2)):
    print(var2[i])
"""
# 8). Python file program to read a file line by line and store it in a list.

# Set result_list blank list variable.
# Open the file with context manager with read mode.
# Initiate an infinite while loop.
# Read each line one by one.
# Check line is black or not and break the loop if it is blank.
# Append the lines in the result_list.
# print the result_list.
"""
result_list=[]
object=open('emp.txt','r')

while True:
    line=object.readline()
    if not line:
        break
    result_list.append(line)
print(result_list)
"""

# 9). Python file program to find the longest word in a file.
"""
obj=open('emp.txt','r')
data=obj.read()
word_list=data.split()

max_word = ''
max_len = 0
for word in word_list:
    #word_len=len(word)
    if len(word) > max_len:
            max_len = len(word)
            max_word = word
    else:
        continue
print(max_word)
"""
"""
obj =open('emp.txt','r')
data=obj.read()
word_list=data.split()
print(word_list)

max_word=''
max_len=0
for word in word_list:
    if len(word)>max_len:
        max_len=len(word)
        max_word=word
print(max_word)
"""

# 10). Python file program to get the count of a specific word in a file.
"""
obj=open('emp.txt','r')
data=obj.read()
word_list=data.split()
count=0
for word in word_list:
    if word=='Language':
        count=count+1
print(count)
"""


# 11). Python file program to read a random line from a file.
"""
def read_specific_lines(filename,line_num):
    with open(filename, "r") as file:
        for i in range(line_num):
            data1 = file.readline()
            print(data1, end="")

read_specific_lines("emp.txt", 5)
"""


# 12). Python file program to copy the file’s contents to another file after converting it to lowercase.

# First read the first file in the reading mode using with open(‘ReadContent.txt’, ‘r’) as data_file.
# Inside the above statement use another statement to read the second file in appending mode using with
# open(‘Writecontent.txt’, ‘a’) as output_file.
# Use a for loop to iterate over lines in the first file.
# Add each line to the second file by using write() after converting the characters in the line to the lowercases using lower()
"""
with open ('emp.txt','r') as data_file:
  with open ('lower_emp','a') as output_file:
      for lines in data_file:
          output_file.write(lines.lower())
"""

# 13). Python file program to copy the file’s contents to another file after converting it to uppercase.
"""
with open ('emp.txt','r') as data_file:
    with open ('upper.txt','a') as output_file:
        for lines in data_file:
            output_file.write(lines.upper())

"""

# 14). Python file program to count all the words from a file.
"""
with open ('emp.txt','r') as data_file:
    word_list=data_file.read().split()
    count=0
    for word in word_list:
        count=count+1
print(count)
"""


# 15). Python file program to sort all the lines File as per line length size.

# Open file in read mode with context manager
with open("emp.txt", "r") as file:
    # Read list of lines.
    FileLines = file.readlines()
    # Initial for loop to start picking each line one by one
    for i in range(len(FileLines)):
        # Initial for loop to compare all remaining line with previous one.
        for j in range(i+1, len(FileLines)):
            # compare each line length, swap small len line with long len line.
            if len(FileLines[i]) > len(FileLines[j]):
                temp = FileLines[i]
                FileLines[i] = FileLines[j]
                FileLines[j] = temp
            else:
                continue

# re-write all the line one by one to the file
with open('ReadContent.txt', "w") as file:
    # Combine all the sequentially arrange lines with join method.
    all_lines = ''.join(FileLines)
    # overwrite all the existing lines with new one
    file.write(all_lines)























































































