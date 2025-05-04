# a-z
# 0-9
# . _ only  1 time
#. comes 2 or 3 place from last 
import re 
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your mail : ")
if re.search(email_condition,user_email):
    print("Right Email")
else:
    print(" Wrong Email")