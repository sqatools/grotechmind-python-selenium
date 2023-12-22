#write Programme to find longest word from given string.

str1="We are Learning Python Programming"

# for var in str1:
#     print(var)

str2= str1.split()
print(str2)
len_word=''
for var in str2:
    print(var,len(var))
    if len_word> var:
        len_word=len(var)
        print(var)


