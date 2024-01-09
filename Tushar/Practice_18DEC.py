#Rule.4
#str[initial_index: last_index: difference]

str1="im learning Python selenium automation"

print("str1:",str1[3:15:1]) #learning Pyt

print("str1:",str1[3:15:2]) #lann y

print("="*100)
#when we use diff value is minus then our initial index is always minus and read from right to left in reverse order

str1="im learning Python selenium automation"

print("str1:",str1[3:15:-1]) #str1: not giving any result due to initial index is positive

print("str1:",str1[-3:15:-1]) #itamotua muineles no

#Rule.5
#str[: last_index: Difference]
#initial index is zero if diff is positive and initial_index is -1 if diff is negative

str1="im learning Python selenium automation"

print(str1[:10:1]) #im learnin # diff is positive so initial indesx is zero  print from left to right

print(str1[:10:-1]) #noitamotua muineles nohtyP  ##diff is negative so initial index is -1 . so print from right to left


#Rule.6
#str[: :  Difference]
#when diff is positive : initial index is zero and last index is end of string .print left to right
#when diff is negative : initial index is -1 and last index is begining of string .print right to left


str1="im learning Python selenium automation"

print(str1[::1]) #im learning Python selenium automation
print(str1[::-1]) #noitamotua muineles nohtyP gninrael mi #if asked reverse the string then used this .

###programme###
###arrange the words as per expection###

str1="Python Programming"
#output="gython ProgramminP"

P_val= str1[0]
g_val=str1[-1]
rem_val=str1[1:-1]
output=g_val+rem_val+P_val
print(output)

str1="Python Programming"
#output="Python Programming Python"

str2=str1[0:6]

print(str1+" " +str2)


###get values from string using loop

str1="Python Programming"
for var in str1:
    print(var)

print("="*100)

###apply loop with indexing

str1="Python Programming"
str_len=len(str1)
print(str_len)
for i in range (str_len):
    print(i)
