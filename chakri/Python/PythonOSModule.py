import os
import shutil

print(os.getcwd())

a = os.getenv('path')
print(a)
b = os.getenv('chakri')
print(b)

#os.mkdir('new-folder1')
getpath = r"C:\Pythonseleniumautomation\gitrepo\pythonseleniumcode\grotechmind-python-selenium\chakri\new-folder1\newfoder2"

#os.mkdir(getpath)
print(os.getcwd())
#os.rmdir('new-folder1')
os.chdir(r"/gitrepo/pythonseleniumcode/grotechmind-python-selenium/chakri/new-folder1")
print(os.getcwd())
#os.mkdir('pk')
#os.rmdir('pk')

a = r'C:\Pythonseleniumautomation\gitrepo\pythonseleniumcode\grotechmind-python-selenium\chakri'
b = os.listdir(a)
print(os.listdir(a))
for file in b:
    print(file)
z = r'C:\Pythonseleniumautomation\gitrepo\pythonseleniumcode\grotechmind-python-selenium'
print(os.path.isdir(z))
print(os.path.isfile(z))


