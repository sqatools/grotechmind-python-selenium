# from Python_OOPS_Programme_Practice import village
#
# obj=village("Bhugav","pune")
# obj.display_village_name()
# obj.dispaly_village_dist()
#
#
# from Python_OOPS_Programme_Practice import movie
# obj=movie("terenam","mar")
# obj.movie_details()


from Python_OOPS_Programme_Practice import son



# from Python_OOPS_Programme_Practice import father
# obj=father("kamala","audi")
# obj.father_details("Dhanora")

class mother:

    def __init__(self,mname):
        self.mother_name=mname

    def mother_details(self):
        print("mother name is:",self.mother_name)

# obj=mother("alka")
# obj.mother_details()
#
obj=son("Santosh",40,"madhavrao","honda")
# obj.son_details()
# obj.father_details("Dhanora")


var1=obj.son_details()
var2=obj.father_details("Dhanora")

print(var1)

str1="tushar"
str2="aher"

print(str1+str2)




