
Str1 = "Learning Python Programming"
# output1 = {'Lg' : 'Learning', 'Pn' : 'Python', 'Pg' : 'Programming'}

str2 = Str1.split()
print(str2)
output = {}
for val in str2:
    first_char = val[0]
    last_char = val[-1]
    result = first_char+last_char
    output[result] = val
    print(output)

print('-'*20)
String = "Learning Python Programming"
print(String)
str1 = String.split()
output = {}
for word in str1:
    first_char = val[0]
    last_char = val[-1]
    result = first_char+last_char
    rev_word = val[::-1]
    output[result]= rev_word
    print(output)









"""for word in word_list:
    first_char = word[0]
    last_char = word[7]
    print(word, first_char)
    print(word, last_char)
    word1 = first_char+ last_char
    print(word1)
    output[word1] = word
    print(output) """
