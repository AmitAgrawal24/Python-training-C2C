from distutils.log import error
from itertools import count
import re

def registration():
    try:
        count=5
        for i in range(5):
            print(f"You have maximum {count} number of attemts to fill the form")
            count=count-1
            l=[]
            print("Enter Name your First Name :")
            first=input()
            while first=="":
                print("First name should not be empty, Mandatry field *")
                first=input()
            reg="^([a-zA-Z]*)$"
            if re.search(reg, first):
                print("Your name first name is ", first)
                l.append(first)
            else:
                print("Your first name is not valid:")
                continue
            print("Enter Name your Last Name :")
            last=input()
            while last=="":
                print("Last name should not be empty, Mandatry field *")
                last=input()
            reg="^([a-zA-Z])*$"
            if re.search(reg, last):
                print("Your name is ", last)
                l.append(last)
            else:
                print("Your name is not valid:")
                continue

            print("Enter your phone no.")
            nu=input()
            if nu.isnumeric() and int(len(nu))==10:
                print("Your phone number is", nu)
                l.append(nu)
            else:
                print("Please Enter the valid number")
                continue
            print("Enter your Prefered city name")
            city=input()
            while city is "":
                print("City should not be empty, it's a mandatory field *")
                city=input()
            reg="^([a-zA-Z]*)$"
            if re.search(reg, city):
                print("Your City name is ", city)
                l.append(city)
            else:
                print("Please Enter the Valid city name")
                continue
            print("Enter your salary Expectation in numberic format")
            salary=input()
            while not re.search("^([0-9]*)$",salary):
                print("Enter salary in proper format")
                salary =input()
            if salary.isnumeric():
                print(f"your salary expectation is {salary}/- ")
                l.append(salary)
            print("Enter your previous company Department")
            department=input()
            while department is "":
                print("Department should not be empty, it's a mandatory field *")
                department=input()
            reg="^([a-zA-Z0-9])*\s*"
            if re.search(reg, department):
                print("Your City name is ", department)
                l.append(department)
            else:
                print("Please Enter the Valid city name")
                continue
            if len(l)==6:
                print("Congratulation!Your registration has done for this job")
                break
        return l
    except error as e:
        print("ERROR| ERROR occured during registration of Applicant", e)
    finally:
        print("Applicant registered sucessfully")

