"""
''' 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.
'''
string =  "Shekhar Tyagi"           # "sqatools"
if len(string) < 2:
	print(True)
else:
	last_string = string[:2]+ "_" +string[-2:]
	print(last_string)


# 2). Python string program that takes a list of strings and returns the length of the longest string.
print("2). Python string program that takes a list of strings and returns the length of the longest string.")

string = ["i", "am", "Shekhar", "Tyagi", "123456789"]
temp = 0
for i in string:
	lenth = len(i)        # 1,2,7,5,9
	print(lenth, end=",")
	if lenth > temp:
		temp=lenth          # 1,2,7,9
print("\n",temp)

"""

