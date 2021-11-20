#This is a SQL sutudent database code.


# Student credentials:

class student():
    def __init__(self):
        self.__fname = ""
        self.__lname = ""
        self.__age = 0
        self.__score = 0

    def get_Fname(self):
       return self.__fname

    def get_Lname(self):
        return self.__lname

    def get_Age(self):
        return self.__age

    def get_Score(self):
        return self.__score
        


    def set_Fname(self, setFname):
        self.__fname = setFname

    def set_Lname(self,setLname):
        self.__lname = setLname

    def set_Age(self, setAge):
        self.__age = setAge

    def set_Score(self, setScore):
        self.__score = setScore

    def update_Fname(self, update_fname):
        if len(update_fname) > 10:
            print("Max 10 chars")

        else:
             self.__fname = update_fname


    def update_Lname(self, update_Lname):

        if len(update_Lname) > 20:
            print("Max 20 chars")

        else:
             self.__lname = update_Lname

    def update_score(self,update_score):
        if 0 <= update_score <= 100:
            self.__score = update_score
        else:
            print("Enter 0-100 score only.")

    def __str__(self):
        return "Student Name:{}\nStudent Last name:{}" \
               "\nStudent Age:{}\nStudent score:{}\n".format(self.__fname, self.__fname, self.__age, self.__score )


