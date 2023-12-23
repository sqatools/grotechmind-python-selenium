#write Programme to find longest word from given string.

str1="We are Learning Python Programming"

# for var in str1:
#     print(var)

word_list= str1.split()
print(word_list)

longest_word=''
long_len=0
for word in word_list:
    print(word,len(word))
    word_len=len(word)
    if word_len>long_len:
        long_len=word_len
        longest_word=word
        print(longest_word)



"""
        
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
"""
stra="happy new year to everyone"
word_list=stra.split()
print(word_list)

longest_word=''
long_len=0
for word in word_list:
    print(word,len(word))
    word_len=len(word)
    if word_len>long_len:
        long_len=word_len
        longest_word=word
        print(longest_word)

print("="*50)

str1="I am Tushar Aher from Nashik Maharashtra"

longest_word=''
long_len=0

word_list=str1.split()
print(word_list)

for word in word_list:
    print(word,len(word))
    word_len=len(word)
    if word_len>long_len:
        longest_word=word
        print(longest_word)




# if word_len>long_len:
#         long_len=word_len
#         longest_word=word
#         print(longest_word)


#program2 : write a python program to maximum repeated character.

str1="We are learning Python Programming, Its very easy to learn"

max_count=0
max_rchar=''
temp=''
for char in str1:
    if char not in temp and char.isspace() is False:
        print(char,str1.count(char))
        char_count=str1.count(char)
        temp=temp+char
        if char_count>max_count:
            max_count=char_count
            max_rchar=char
print(max_rchar)
print(max_count)


































