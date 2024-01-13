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
'''
a = {'Name' : 'John', 'Age' : 25}
b = {'email' : 'john@gmail.com', 'Address' : 'Mumbai'}

a.update(b)
print("a :",a)

c = a.pop('Name')
print(a)
print(c)
print(a.keys())
print(a.values())
b = a.items()
print(type(b))
b = list(b)
print(b[0])








