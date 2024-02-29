import os
import shutil

##get current working directory:os.getcwd()

print("cwd",os.getcwd())


# Get list of files and folder available on the target path

target_path=r"D:\cfrbackup-FFAVJEMP"
dir_data=os.listdir(target_path)
print(dir_data)

print(len(dir_data))


# Create folder on target path

target_path=r"D:\Namaste Python\Day-04"
#os.mkdir(target_path)

#remove directory and file from path

folder_path=r"D:\Namaste Python\Day-04"
#os.removedirs(folder_path)# remove the folder/directory

file_path=target_path=r"D:\Namaste Python\Day-04"
#os.remove(file_path)


# join two path with os.path.join

file_name="tests.txt"
folder_path=r"D:\Namaste Python\Day-04"

file_path = os.path.join(folder_path,file_name)
print("file path :", file_path)  #file path : D:\Namaste Python\Day-04\tests.txt

# Check given folder is available on target path or not

file_path : r"D:\Namaste Python\Day-04\test.txt"

output=os.path.isdir(file_path)
print(output) #True

#output=os.path.isdir()










