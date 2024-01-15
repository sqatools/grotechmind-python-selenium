def readfile(filename):
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

