'''def readfile(filename):
    a = open(filename,'r')
    data = a.read()
    print(data)
    a.close()

#readfile('chakri.txt')

def addfile(filename,content):
    a = open(filename,'w')
    a.write(content)
    a.close()


#addfile('chakri','hello guys happy sankaranti')
#addfile('chakri','hello depeesh')
#readfile('chakri')
def appendfile(filename,content):
    a = open(filename,'a')
    a.write(content)
    a.close()

#appendfile('chakri','hello deepsh happy pongal')
readfile('chakri')




def writefile(filename,content):
    a = open(filename,'w')
    a.write(content)
    a.close()
'''

def writefile(filename,c):
    a = open(filename,'w')
    a.write(c)
    a.close()

writefile('chakri.txt', 'who are you')

def readfile(filename):
    a = open(filename)
    b = a.read()
    print(b)
    a.close()

readfile('chakri.txt')

def appendfile(filename,c):
    a = open(filename,'a')
    a.write(c)
    a.close()

appendfile('chakri.txt', ' , i am chakri')
readfile('chakri.txt')
writefile('chakri.txt', 'work hard to get a good job')
readfile('chakri.txt')
appendfile('chakri.txt', '  thanks for your concern i  am trying my level best')
readfile('chakri.txt')

writefile('chakri.txt', 'python file handling')
readfile('chakri.txt')





















































