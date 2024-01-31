str1= 'learning python program'
word_list=str1.split()
output= {}

for i in word_list:
    first_char=i[0]
    output[first_char]=i
print(output)



