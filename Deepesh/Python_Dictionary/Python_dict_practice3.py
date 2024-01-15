# write a python program to get below output

str1 = "Hello Good Morning"
#output = {'H' : 'Hello', 'G' : 'Good', 'M' : 'Morning'}

"""
-> get word list from string, str1.split()
-> iterate through each word using loop : for word in word_list
-> get first character of each word using indexing : word[0]
-> store the first as key and word as value
"""
output = {}
# output['name'] = 'saumya'
word_list = str1.split()
print(word_list)
for word in word_list:
    first_char = word[0]
    print(word, first_char)
    output[first_char] = word
    #stringoutput[str3] = i
    print(output)

print(output)

# class work
str1 = "Learning Python Programming"
# output1 = {'Lg' : 'Learning', 'Pn' : 'Python', 'Pg' : 'Programming'}


# output2 = {'Lg' : 'gninraeL', 'Pn' : 'nohtyP', 'Pg' : 'gnimmargorP'}


# Home work
# word[::-1]
str1 = "Programming"
print(str1[::-1])
print(str1[-1:-len(str1)-1 :-1])
# program1
list1 = [4, 7, 8, 9]
list2 = [1, 6, 5, 2]
#output = {4: 1, 7:36, 8 : 25, 9:4}

# program2:
str1 = "We are learning Python Programming"
output =  {'W2' : 'wE', 'a3' : 'ARE', 'l8' : 'LEARNING', 'P6': 'pYTHON', 'P11': 'pROGRAMMING'}
"""
-> get word list : split method
-> get first char
-> get length of each word 
-> combine both length and first char
-> change the lower character upper and upper to lower.
-> Add both values in dict output
"""
output = {}
word_list = str1.split()
for word in word_list:
    first_char = word[0]
    word_len = len(word)
    swap_case_val = word.swapcase()
    #output[f"{first_char}{word_len}"] =  swap_case_val
    output[first_char+str(word_len)] = swap_case_val

print("output :", output)

















