#Enter Class and Student Names


#input("Select your Class 1st to 5th " )
var1 = input("Select your Class 1st to 5th " )
classes=['1','2','3','4','5']
for i in range(len(classes)):
    if classes[i]==var1:
        #Name = input("Enter Student Name ")
        #classs = input("Enter Class Name ")
        student1={ "Name":'Rahul', "classe":'john'}
        print(student1)
    else:
        print("user input didn't match")


