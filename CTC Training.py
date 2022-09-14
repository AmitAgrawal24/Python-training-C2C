from itertools import count
import re

count=5
for i in range(5):
    print(f"You have maximum {count} number of attemts to fill the form")
    count=count-1
    l=[]
    print("Enter Name")
    name=input()
    reg="([a-zA-Z])*\s*"
    if re.search(reg, name):
        print("Your name is ", name)
        l.append(name)
    else:
        print("Your name is not valid:")
    print("Enter your age")
    age=input()
    if age<0 or not age.isnumeric():
        print("Please Enter the valid age")
    elif age <18:
        print("You are not the Eligble Person as your age is less than 18")
    elif age >60:
        print("You are over age for this job")
    else:
        l.append(age)
        print("Your age is ", age)
    print("Enter your phone no.")
    nu=input()
    if nu.isnumeric() and nu==10:
        print("Your phone number is", nu)
        l.append(nu)
    else:
        print("Please Enter the valid number")
    if len(l)==3:
        print("Congratulation!Your registration has done for this job")
        break
print(l)
