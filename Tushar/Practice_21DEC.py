#12.Join Method

str1="I am learning join method to join string with any other defind string or anything"

print("_".join(str1))

#I_ _a_m_ _l_e_a_r_n_i_n_g_ _j_o_i_n_ _m_e_t_h_o_d_ _t_o_ _j_o_i_n_ _s_t_r_i_n_g_ _w_i_t_h_ _a_n_y_ _o_t_h_e_r_ _d_e_f_i_n_d_ _s_t_r_i_n_g_ _o_r_ _a_n_y_t_h_i_n_g

print("a".join(str1))

#Ia aaama alaeaaaranaianaga ajaoaiana amaeatahaoada ataoa ajaoaiana asataraianaga awaiataha aaanaya aoatahaeara adaeafaianada asataraianaga aoara aaanayatahaianag


###if we want _ after each 2 char

stra="python"

result=""
for i in range (len(stra)):
    if i%2==0 and i!=0:
        result=result+"*"+stra[i]
    else:
        result=result +stra
        [i]
print("result:",result)



###programme for reverse the string#############


str="Python Programming"

output=""
for i in range (-1,-len(str)-1,-1):
    #print(i)
    output=output+str[i]
    print(output)

#13. strip: this method removes the trailing spaces from given string
#space available before and after the string is known as trailing space.

str2=" I am learning strip method to remove trailing spaces "
print(str2) # I am learning strip method to remove trailing spaces

print(str2.strip()) #I am learning strip method to remove trailing spaces

print(str2.lstrip()) #remove left space of start of string
print(str2.rstrip()) # remove right space of end of string

#14. isspace

str="python isspace method"

print(str.isspace()) #False

for char in str:
    print(char,":",char.isspace())

##############

strv="hello programme"

print(strv.replace(' ',' -')) #hello -programme

print("="*100)

#########################################

result=""
for char in strv:
    if char.isspace():
        result=result+"- "
    else:
        result=result+char
print(result)

#hello- programme


