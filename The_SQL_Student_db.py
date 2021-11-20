import sqlite3
from Sudents import *

s1 = student()
s1.update_Fname("Moshe")
s1.update_Lname("Moshayev")
s1.set_Age(50)
s1.update_score(80)

s2 = student()
s2.update_Fname("Shmaker")
s2.update_Lname("Fuls")
s2.set_Age(80)
s2.update_score(45)

s3 = student()
s3.update_Fname("Kosta")
s3.update_Lname("Rasputin")
s3.set_Age(12)
s3.update_score(100)

data = sqlite3.connect("StudentData.db")

sdata = data.cursor()

sdata.execute("""CREATE TABLE Students (
                'First Name' TEXT,
                'last Name' TEXT,
                 Age  INT,
                 Score INT)""")

sdata.execute("INSERT INTO Students VALUES ('{}', '{}', {}, {})".format(s1.get_Fname(), s1.get_Lname(), s1.get_Age(), s1.get_Score()))
sdata.execute("INSERT INTO Students VALUES ('{}', '{}', {}, {})".format(s2.get_Fname(), s2.get_Lname(), s2.get_Age(), s2.get_Score()))
sdata.execute("INSERT INTO Students VALUES ('{}', '{}', {}, {})".format(s3.get_Fname(), s3.get_Lname(), s3.get_Age(), s3.get_Score()))
sdata.execute('SELECT * FROM Students')
print(sdata.fetchall())
data.commit()
data.close()