#1. Write a python program to find the longest word from given string
str1 = "We are learning Python Programming, Its very easy to learn"
word_list = str1.split()
print(word_list)
longest_word = ''
long_len = 0 # 2, 3, 8, 12

# for ankita in str1:
#     print(ankita)

for word in word_list:
    print(word, len(word))
    word_len = len(word) # 2, 3, 8, 6, 12, 3, 4, 5, 5
    if word_len > long_len: # | 2> 0 | 3 > 2| 8 > 3 | 6 > 8 | 12 > 8 | 3 > 12 | 4> 12 | 4> 12 | 5 > 12
        long_len = word_len # 2, 3, 8, 12
        longest_word = word # We, are, learning, Programming,
        print("longest word :",  longest_word)
    print("_"*40)

print("Longest word :", longest_word)

list1  = [5, 7, 8, 23, 5]
print(max(list1))


#####
# program2 : write a python program to maximum repeated character.
print("_"*40)

str1 = "We arePPP learning Python Programming, ItPPPPPs very easy to learn"
max_count = 0
max_rchar = ''
temp = '' #Wea
for char in str1:
    if char not in temp and char.isspace() is False:
        print(char, str1.count(char))
        char_count = str1.count(char) #W=1, e=6, a =5, r=6, P = 10
        temp = temp + char # Wear
        if char_count > max_count: # 1 > 0 | 6 > 1 | 5 > 6 | 6 > 6 | 10 > 6
            max_count = char_count # 1, 6, 10
            max_rchar = char # W, e, P


print("max count", max_count)
print("max repeated char :", max_rchar)
