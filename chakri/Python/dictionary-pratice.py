'''print("_"*50)
dictf = {'email' : 'john@gmail.com', 'Address' : 'Mumbai', 'Phone': 56656435}

#var = dictf.pop('Phone')
#print(dictf)
#print("var :", var)
a = dictf.popitem('email')
print(a)'''
dictf = {'email' : 'john@gmail.com', 'Address' : 'Mumbai',
         'Phone': 56656435, 'country' : 'India'}

'''var2 = dictf.popitem()
#print(var2)
for i in range(len(dictf)):
    print("dictf :", dictf)
    print(dictf.popitem())
a = dictf.get('email')
print(a)
for key,val in dictf.items():
    print(key,val)
b = dictf.items()
print(b)
print(list(b)[0][1])

c = {'r' : 'ramu', 's' : 'sainath', 'b' : 'rdm', 'p' : 'prasanna' }
c['c'] = 'chakri'
print(c)
d = c
d['n'] = 'naga mani sai'
print(c)

e = c.copy()
e['mobile'] = 9154660350
print(e)
del e['mobile']
print(e)'''
school = {

    'teacher' : {
        'math' : [{'Name' : 'mohan', 'email' : 'mohan@gamil.com', 'phone' : 656546556}],
        'physics' : [ {'Name' : 'Rahul Gupta', 'email' : 'rahul@gmail.com', 'phone' : 7765766765},
                      {'Name' : 'Sanjay', 'email' : 'sanjay@gmail.com', 'phone' : 8889998848}, ],
        'chemistry' : [ {'Name' : 'Mohit Jain', 'email' : 'mohit@gmail.com', 'phone' : 546456546}]
    },
    'students': {
        '9th': [
            {'Name': 'krishna', 'email': '9st1@gmail.com', 'phone': 54643564},
            {'Name': 'chandu', 'email': '9st2@gmail.com', 'phone': 656567547},
        ],
        '10th': [
            {'Name': 'rdm', 'email': '10st1@gmail.com', 'phone': 8888888},
            {'Name': 'prasanna', 'email': '10st2@gmail.com', 'phone': 33334444},
            {'Name': 'ramu', 'email': 'mohit@gmail.com', 'phone': 9666004249},
        ],
        '11th': [
            {'Name': 'sainath', 'email': '11st1@gmail.com', 'phone': 999999},
            {'Name': 'pavan', 'email': '11st2@gmail.com', 'phone': 222322233},
        ],
        '12th': [
            {'Name': 'chakri', 'email': '12st1@gmail.com', 'phone': 65656565},
            {'Name': 'harsha', 'email': '12st2@gmail.com', 'phone': 353535353},
            {'Name': 'mokshi', 'email': 'mohit123@gmail.com', 'phone': 435435345}
        ],


    }
}
'''
for key,value in school.items():
    for k1,v1 in value.items():
        print(k1)
        if k1 == '11th':
            for data in v1:
                if data['Name'] == '11st2':
                    print(data['phone'])

for key,value in school.items():
    for k1,v1 in value.items():
        #print(k1)
        if k1 == 'math':
            for data in v1:
                print(data['email'])

for key,value in school.items():
    for k1,v1 in value.items():
        if k1 == '10th':
            for data in v1:
                if data['Name'] == 'ramu':
                    print(data)
                    print(data['phone'])
 'clear', 'copy', 'fromkeys', 'get', 'items', 
 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

a = {'a': 78,'b': 'chakri','c':[1,2,3],'d':(1,2,3,3,5)}
#print(type(a))
a['e'] = 'king'
#print(a)
#print(a['d'])
a[5] = {4, 7, 8}
a[4.5] = [5, 8, 2]
a[(5, 7, 9)] = {'Name' : 'john', 'age' : 25}
a[True] = False
print(a)

a = {'Name' : 'John', 'Age' : 25}
b = {'email' : 'john@gmail.com', 'Address' : 'Mumbai'}

a.update(b)
'''#print("a :",a)

'''c = a.pop('Name')
print(a)
print(c)
print(a.keys())
print(a.values())
b = a.items()
print(type(b))
b = list(b)
print(b[0])
'shallow copy'
a = b
b['age'] = 25
print(a)
c = a.copy()
c['qualification'] = 'graduation'
print('c:',c)
print('a :',a)

print(a)
del a['Age']
print(a)
b = a.setdefault('job','tests engineer')
print(a)
print(b)
#1). Python Dictionary program to add elements to the dictionary.
a = {'a': 3,'b':67,'c': 'mokshi','d': 'chakri','age': 25,'frnd': ['sainath','ramu','prasanna']}
a.setdefault('city','savaram')
for key,value in a.items():
    print(key,':',value)
    
#2). Python Dictionary program to print the square of all values in a dictionary.
a = {'a':6,'b':7,'c':8,'d':10}
for key,value in a.items():
    print(key,';',value)
#3). Python Dictionary program to move items from dict1 to dict2.
a = {'a':6,'b':7,'c':8,'d':10}
b = {}
print(b)
b.update(a)
print(b)

#4). Python Dictionary program to concatenate two dictionaries.
dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age' : 25, 'salary': '$25k'}
dict1.update(dict2)
print(dict1)

#5). Python Dictionary program to get a list of odd and even keys from the dictionary.
a = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
#Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
#Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
even = []
odd = []
for k,v in a.items():
    if k%2 == 0:
        e = k,v
        even.append(e)
    else:
        o = k,v
        odd.append(o)
print('even :',even)
print('odd :',odd)

#6). Python Dictionary Program to create a dictionary from two lists.
a = ['a', 'b', 'c', 'd', 'e']
b = [12, 23, 24, 25, 15, 16]
#Output :
#{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}
c = { }
for i in a:
    for k in b:
        if a.index(i) == b.index(k):
            c.setdefault(i,k)
print(c)

#7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
a = [4, 5, 6, 2, 1, 7, 11]
#Output :{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
b = {}
for i in a:
    if i%2 == 0:
        c = i**2
        b.setdefault(i,c)
    else:
        d = i**3
        b.setdefault(i,d)
print(b)

#8). Python Dictionary program to clear all items from the dictionary.
a = {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
a.clear()
print(a)

#9). Python Dictionary program to remove duplicate values from Dictionary.
a = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
#Output :{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
b = []
c = {}
for k,v in a.items():
    if v not in b:
        b.append(v)
        c.setdefault(k,v)
print(c)
for k1,v1 in a.items():
    if v1 not in a.values():
        c.setdefault(k1,v1)
        #c[k1] = v1
print(c)

#10). Python Dictionary program to create a dictionary from the string.
a = 'SQATools'
#Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
b = {}
for i in a:
    if i not in b.keys():
        c = a.count(i)
        b.setdefault(i,c)
print(b)
'''
#11). Python Dictionary program to sort a dictionary using keys.
a = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
for k,v in a.items():
    print((k,v))





























