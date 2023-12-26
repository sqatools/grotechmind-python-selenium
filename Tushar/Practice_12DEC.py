### write programme to cal factorial of any given no##############

#5=5*4*3*2*1
num=6
fact=1
for i in range (num,0,-1):
    print(i)
    fact=fact*i
    print("fact:" ,fact)

###writ a programme to print fabonaci series

#a b a+b  a   b   a   b   a
# b     a
#0,1, 1,  2,  3,  5,  8,  13,   21   ,34.,
#  a  b  a+b     a+b      a+b         a+b
#a=b
#b=a+bd

a=0
b=1
for i in range (10):
    print(b,end=" ") ##by default print fun have /n means it prints on next line so here used end " " to print op in single line
    a,b=b,a+b

print("="*50)
#write python programme to find the given number is prime or not
#prime number: the number which can divide by 1 or the number itself.
##1,2,3,5,7,11,13,17,19,23......

num1=11
prime=True
for i in range (2,num1):  ###num1//2
    #print("i:",i)
    if num1%i==0:
        prime= False
        #break
if prime:
    print("This is prime number:",num1)
else:
    print("This is not prime number:",num1)

print("+"*50)
