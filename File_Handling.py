def file_add(filename):
     obj1= open(filename,'r')
     data=obj1.read()
     print(data)
     file_add("test.txt")

