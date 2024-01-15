def read_file(text):
    obj1 = open(text,'r')
    data = obj1.read()
    print(data)
#read_file("text.txt")


def write_file(text,content):
    obj1 = open(text,'w')
    data = obj1.write(content)
    print(data)
#write_file("text.txt","hi")

def write_new_file(text1,content):
    obj1 = open(text1,'w')
    data = obj1.write(content)
    print(data)
#write_new_file("text1.txt","hi")

def append_file(text1,content):
    obj1 = open(text1,'a')
    data = obj1.write(content)
    print(data)
#append_file("text1.txt","my name is tushar")
append_file("text2.txt","my name is tushar")


