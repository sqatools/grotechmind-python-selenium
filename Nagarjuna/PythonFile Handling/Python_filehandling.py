"""
File opening mode
Read mode (r)
Write mode (w)
apend mode (a)
"""

def read_file(filename):
    obj1 = open(filename, 'r')
    data = obj1.read()
    print(data)
    obj1.close()
