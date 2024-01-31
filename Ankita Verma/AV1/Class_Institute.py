# Institute Class Structure
"""Class institute
Student---(Bca,Mca,Mtech,CS)
departments(Admin,Computer department,
faculty """


class institute_I:
    def __init__(self,stu_name,stu_course,stu_roll):
        self.student=stu_name
        self.stu_course=stu_course
        self.stu_roll=stu_roll


class student_i:
     def __init__(self,bca,mca,mtech,cs):
         self.bca=bca
         self.mca=mca
         self.mtech=mtech
         self.cs=cs

class faculty_i:
      def __init__(self,f_Name,f_Qualificatin,f_assigned):
           self.f_Name=f_Name
           self.f_qualification=f_Qualificatin
           self.f_assigned=f_assigned
