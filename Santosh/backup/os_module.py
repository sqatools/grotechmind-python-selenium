import os
import shutil

# Get current work directory
"""
curr_dir = os.getcwd()
print(curr_dir)
"""

# Get list of files and folder available on the target path
"""
tar_path = "E:\\Filesdata"
dir_data = os.listdir(tar_path)
print(dir_data)

print(len(dir_data))

"""
# Create folder on target path
"""
folder_path ="E:\\Filesdata\\new_dir\\BI10"
os.mkdir(folder_path)
"""

#remove directory and file from path
"""

folder_path ="E:\\Filesdata\\new_dir\\BI10\\testfolder"
file_path = "E:\\Filesdata\\new_dir\\BI10\\BI10_test.txt"
os.removedirs(folder_path) # directory should be empty
os.remove(file_path) # it removes the file from path

"""

# join two path with os.path.join
"""
filename = "BI10_test.txt"
folder_path ="E:\\Filesdata\\new_dir\\BI10"

file_path = os.path.join(folder_path, filename)
print("file path :", file_path)
"""


# Check given file is available on target path or not
"""
file_path = "E:\\Filesdata\\new_dir\\BI10\\BI10_test1.txt"
output = os.path.isfile(file_path)
print("output:", output)
"""

# Check given folder is available on target path or not
"""
folder_path = "E:\\Filesdata\\new_dir\\BI10\\testfolder"
folder_path2 = "E:\\Filesdata\\new_dir\\BI10\\testfolder1"
output = os.path.isdir(folder_path)
print("output:", output) # True

output2 = os.path.isdir(folder_path2)
print("output2:", output2) # False
"""

# Program: find out list of folder and files in target path.
"""
-> get list of files and folder os.listdir(path)
-> get path of each file and folder using loop and os.path.join
-> check each path is file or folder using isfile and isdir method.
-> Append files and folder in two separate list as per check.
"""
"""
tar_path = "E:\\Filesdata"
file_list = []
dir_list = []
dir_data = os.listdir(tar_path)

for data in dir_data:
    #print(data)
    data_path = os.path.join(tar_path, data)
    if os.path.isfile(data_path):
        file_list.append(data)
    elif os.path.isdir(data_path):
        dir_list.append(data)
    else:
        continue

print("File list:", file_list)
print("Directory list:", dir_list)
"""


################### copy data using shutil #############
src_path = "E:\\Filesdata\\new_dir\\count_name.txt"
tar_path = "E:\\Filesdata\\new_dir\\BI10\\count_name.txt"

shutil.copy(src_path, tar_path)

