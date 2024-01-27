# Print below string
# Hellow, "I am an engineer"
Var='''Hellow, "I am an engineer" '''
print(Var)

var2="Hellow,\"I am an engineer"
print(var2)
##############################################################################
# How to print below 3 line string

# long_txt_msg= I am santosh workign at "Infosys"
#               Currently living in pune loaction
#               i have very good experince

long_txt_msg=''' I am santosh workign at "Infosys"
Currently living in pune "loaction"
i have very good experince '''
print(long_txt_msg)

#################################################################################

Me="Santosh"
a="This is %s"%Me
print(a)
#OutPut=This is Santosh

Me="Santosh"
a="This is %sssss"%Me
print(a)
#OutPut=This is Santoshssss

#######################################################################################
# (F-string)--String formating
print("*"*50)
A="Santosh"
B="Wadikar"
c=100
var3=f"this is {A} {B} {c}"
print(var3)

############################################################
print("*"*50)
A="Santosh"
B="Wadikar"
c=100
var4=f"this is {A} {B} {c} {40-50}"
print(var4)

########################################################

var10="harry"

print(len(var10))
print(var10[-4:-2])
print(var10[1:3])
print(var10[::-2])

########################################################
print("*"*60)
var11="happy new year 2024"
# display only "new" from above string with +ve & -Ve indexing

print(var11[6:3])
print(var11[6:6])
#output= blank-nothing(bcz it will start from 6 & end with 3 So nothing . It will not maks sence)

print("*"*60)
#with +ve indexing
print(var11[6:9]) #OUTPUT=new

#with -ve indexing
#print(var11[-13:-10])  #OUTPUT=new
print("*"*60)
var11="happy new year 2024"
print(var11[6:9])
print(var11[-13:9])
#9=happy new
print(var11[-13:-10])
print("*"*60)
print(var11[15:-1])
#5=happy
#-5= 2024
#-15=y new year 2024
#15=happy new yearr2
#-5=r2024
print("*"*60)
print(var11[2:4])
print(var11[-17:-15])
print(var11[-17:4])
print("*"*60)
var11="veryhappyear2024"
#var11="python"
print(var11[-5:-4])
print("*"*60)
var11="veryhappyear2024"
print(var11[-3:-8:-2])
print(var11[-3:8:-2])
print(var11[-8::-2])
print(var11[-12:-16:-2])
print(var11[16:12])
print(var11[-5:-9:-2])
print(var11[-4])
print(var11[::-1])


























