#########################42). Python file program to replace space by an underscore in a file.


# Open the first file using open(“readcontent.txt”,”r”).
# Read the data in the file using read().
# Replace the space in the data with “_” using replace() and store the output in the new variable.
# Open the second file using open(“writecontent.txt”,”w”).
# Write the new data in the second file using write().

# # Open file in read mode
# f1=open("readcontent.txt","r")
# # Read data
# data=f1.read()
# # Replace space by underscore
# data=data.replace(" ","_")
# # Open file in write mode
# f2=open("file2.txt","w")
# # Write new data to file
# f2.write(data)

# def replace_file_space(filename):
#     with open(filename,"r") as file1:
#         data=file1.read()
#         data=data.replace(" ","_")
#         file2=open("replace_file_space1","w")
#         file2.write(data)
#         print(file2)
#
# replace_file_space("first txt file.txt")

#########################
#Program to display words from a file that has less than 5 characters

# def read_less_than_5_char_word_from_file(filename):
#     with open(filename,"r") as file:
#         data=file.read().split()
#         for words in data:
#             if len(words)<=5:
#                 print(words, end=" ")
#
# read_less_than_5_char_word_from_file("first txt file.txt")

#########################
#print("*"*60)

# # open file read mode
# f1=open("first txt file.txt",'r')
# # open file in append mode
# f2=open('writecontent.txt','a')
# # Read lines from the file
# lines=f1.readlines()
# # Iterate over lines
# for line in lines:
# # Check for t in the lines
#     if 't' in line:
#     # Write lines to writecontent.txt file
#         f2.write(line)
# f1.close()
# f2.close()
##########################################################################
print("*"*60)

#38). Python file program to count the total number of vowels in a file.


f1=open("../first txt file.txt", 'r')
data=f1.read()
vowel=("a","A","e","E","i","I","o","O","U","u")
if data in vowel:
    





