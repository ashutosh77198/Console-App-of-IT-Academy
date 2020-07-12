import sys
import csv
import os
from datetime import date, timedelta

class Account:
    accNo = 0
    name = ''
    address=''
    gender=''
    email=''
    deposit = 0


    def createAccount(self):
        self.accNo = int(input("Enter the account no for registration : "))
        self.name = input("Enter the Student name : ")
        self.address = input("Enter your current address: ")
        self.gender = input("Enter the gender type : ")
        self.email = input("Enter the Student Email : ")
        self.deposit = int(input("Enter The Initial amount to Register either 20000 or 10000 if you want to pay in installements"))
        with open('info.txt', 'a', newline= '') as studentfile:
            studentfileWriter = csv.writer(studentfile)
            if self.deposit >= 10000:
                studentfileWriter.writerow(
                    [self.accNo, self.name, self.address, self.gender, self.email, self.deposit])
                print("Record has been written to file")
                studentfile.close()
                menu()
            else:

                if self.deposit<=10000:
                    dt = date.today() + timedelta(10)
                    print("Please pay the remaining amount by date:", dt)
                    print("For now we will add your details to our  database")
                    studentfileWriter.writerow(
                        [self.accNo, self.name, self.address, self.gender, self.email, self.deposit])
                    print("Record has been written to file")
                    studentfile.close()
                    menu()





def coursedetails():
    print("\n")
    print("    COURSE OF STUDY      ")
    text_file = open('studentfile.txt', 'r')
    line_list = text_file.read();
    print(line_list)
    print("/////////////////*****IF YOU WANT TO JOIN THE COURSE OF OUR ACADEMY PLEASE ENTER YOUR DETAILS IN OPTION [B]****//////////////////")
    text_file.close()
    menu()
def viewstudentdetails():

    # Open the file for reading
    f = open("info.txt", "r", encoding="utf8")
    displaylist = csv.reader(f)
    dt = date.today() + timedelta(10)
    for i in displaylist:
        print("\n")
        print(i)
        balance= int(i[5])
        print("Total Balance in your account for Registration is :", balance)
        if balance>=20000:
            remaining_balance = balance-20000
            print("**************Please withdraw the money after complition of course***************")
            print("**********************THANK YOU!!!!***********************")
            print("Remaining Balance to be receive after the Regitration is :", remaining_balance)
        else:
            due= 20000-balance
            print("**************Please deposit the money before complition of course***************")
            print("**********************THANK YOU!!!!***********************")
            print("Amount {} still needed to be paid for the Registration by date {}". format(due, dt))

    #print(displaylist)
    f.close()
    menu()
def modistudentdetails():

    num=input("enter the account number to be modified")
    with open('info.txt', 'r+',newline='') as f:
        ro=csv.reader(f)
        rows=[]
        for rec in ro:
            rows.append(rec)
        for i in range(len(rows)):
            if rows[i][0]== num:
                rows[i][1]=input("enter a new name")
                rows[i][2] = input("enter a address")
                rows[i][3] = input("enter a gender")
                rows[i][4] = input("enter a email")
                rows[i][5] = int(input("enter a deposit"))

    print(rows)
    with open('info.txt', 'w', newline='') as f:
        wo=csv.writer(f)
        wo.writerows(rows)
    f.close()
    menu()
def delestudentdetails():
    num=input("Enter the account number of a student that is to be deleted")
    with open('info.txt', 'r+',newline='') as f:
        ro=csv.reader(f)
        rows=[]
        sows=[]
        for rec in ro:
            rows.append(rec)
        for i in range(len(rows)):
            if rows[i][0]!=num:
                sows.append(rows[i])
        #print(sows)
        print("*********The Account Number of choice has been deleted permanently, SORRY!!!!!!********")

    with open('info.txt', 'w', newline='') as f:
        wo=csv.writer(f)
        wo.writerows(sows)
    f.close()
    menu()

def menu():
    datetoday=date.today()

    print("***********************************   IT ACADEMY   **************************************")
    print("**********************************  Kathmandu,Nepal  ************************************")
    print("*****************************  Created By: ASHUTOSH VERMA  ******************************")
    print(' Date of Today :', datetoday)
    print("\n")
    choice = input(
        """A: Enter Course study  details
B: Enter Student details here!!
C: View student details.
D: Modify students details.
E: Delete students details.
Q: Quit.
Please enter your choice: """)

    if choice == "A" or choice == "a":
        coursedetails()
    elif choice=="B" or choice=="b":
        student=Account()
        student.createAccount()
    elif choice == "C" or choice == "c":
        viewstudentdetails()
    elif choice == "D" or choice == "d":
        modistudentdetails()
    elif choice == "E" or choice == "e":
        delestudentdetails()
    elif choice == "Q" or choice == "q":
        sys.exit()
    else:
        print("You must only select either A,B,C,D or Q.")
        print("Please try again")
        menu()
menu()







