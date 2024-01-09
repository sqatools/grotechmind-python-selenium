school = {

    'teacher' : {
        'math' : [{'Name' : 'mohan', 'email' : 'mohan@gamil.com', 'phone' : 656546556}],
        'physics' : [ {'Name' : 'Rahul Gupta', 'email' : 'rahul@gmail.com', 'phone' : 7765766765},
                      {'Name' : 'Sanjay', 'email' : 'sanjay@gmail.com', 'phone' : 8889998848}, ],
        'chemistry' : [ {'Name' : 'Mohit Jain', 'email' : 'mohit@gmail.com', 'phone' : 546456546}]
    },
    'students': {
        '9th': [
            {'Name': '9st1', 'email': '9st1@gmail.com', 'phone': 54643564},
            {'Name': '9st2', 'email': '9st2@gmail.com', 'phone': 656567547},
        ],
        '10th': [
            {'Name': '10st1', 'email': '10st1@gmail.com', 'phone': 8888888},
            {'Name': '10st2', 'email': '10st2@gmail.com', 'phone': 33334444},
            {'Name': 'mohit', 'email': 'mohit@gmail.com', 'phone': 666777666},
        ],
        '11th': [
            {'Name': '11st1', 'email': '11st1@gmail.com', 'phone': 999999},
            {'Name': '11st2', 'email': '11st2@gmail.com', 'phone': 222322233},
        ],
        '12th': [
            {'Name': '12st1', 'email': '12st1@gmail.com', 'phone': 65656565},
            {'Name': '12st2', 'email': '12st2@gmail.com', 'phone': 353535353},
            {'Name': 'mohit', 'email': 'mohit123@gmail.com', 'phone': 435435345}
        ],


    }
}
#print(school['teacher']['physics'][0]['phone'])
#print(school['students']['10th'][1]['phone'])

"""
st_name = '9st1'
st_class = '9th'

for key, value in school.items():
    #print(key)
    for k1, v1, in value.items():
        #print(k1, v1)
        if k1 == '9th':
            #print(v1)
            for data in v1:
                #print(data['Name'])
                if data['Name'] == st_name:
                    print(data['phone'])

"""
# get student details with name
st_name = 'mohit'

for k1, v1 in school.items():
    print(k1)
    if k1 == 'students':
        for k2, v2 in v1.items():
            #print(v2)
            for data in v2:
                #print(data['Name'])
                if data['Name'] == st_name:
                    print(k2, data)


