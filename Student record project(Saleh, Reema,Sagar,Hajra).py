studentList = []  # Creates a list to hold student rec


class student:  # Creates a student class and initialises parametres
    def __init__(self, firstname, surname, department, dor, mobileno, email, home):
        self.firstname = firstname
        self.surname = surname
        self.department = department
        self.dor = dor
        self.mobileno = mobileno
        self.email = email
        self.home = home


class Admin(student):  # New admin class, child class for student inheriting all its properties
    id = "Admin"  # Admins default log-in credentials
    password = "1234"

    def __init__(self, firstname, surname, department, dor, mobileno, email, home):
        super().__init__(firstname, surname, department, dor, mobileno, email, home)

    def Verification(self, id, password):  # Function to verify admin credentials
        if id == self.id and password == self.password:
            return True
        else:
            return False

    def changePassword(self, newPass):  # Function to change password to newPass
        self.password = newPass

    def AddRecord(self, Firstname, surname, department, dor, mobileno, email,
                  home):  # Function to add record to the student list
        objectstud = student(Firstname, surname, department, dor, mobileno, email, home)
        studentList.append(objectstud)

    def DisplayRecords(self, studobject):  # Function to display students' records
        print("First name   : ", studobject.firstname)
        print("Surname : ", studobject.surname)
        print("Department : ", studobject.department)
        print("Date of Registration : ", studobject.dor)
        print("Mobile number   : ", studobject.mobileno)
        print("Email : ", studobject.email)
        print("Home address : ", studobject.home)
        print("\n-----------------------------------------------------------------")

    def SearchRecord(self, surname):  # Function to search students records
        for i in range(studentList.__len__()):
            if studentList[i].surname == surname:  # Iterate through studentList and search record by surname passed
                return i


    def ModifyRecord(self, emailaddress, modificationchoice, updatedvalue):  # Function to modify student records
        studToModify = moderator.SearchRecord(emailaddress)  # Search the records for exact student
        if modificationchoice == 1:  # Then depending on the users modification choice
            studentList[studToModify].firstname = str(
                updatedvalue)  # The specific record is updated with passed updated value
            moderator.DisplayRecords(studentList[studToModify])  # Print the updated student record

        elif modificationchoice == 2:
            studentList[studToModify].surname = str(updatedvalue)
            moderator.DisplayRecords(studentList[studToModify])

        elif modificationchoice == 3:
            studentList[studToModify].department = str(updatedvalue)
            moderator.DisplayRecords(studentList[studToModify])

        elif modificationchoice == 4:
            studentList[studToModify].dor = str(updatedvalue)
            moderator.DisplayRecords(studentList[studToModify])

        elif modificationchoice == 5:
            studentList[studToModify].mobileno = str(updatedvalue)
            moderator.DisplayRecords(studentList[studToModify])

        elif modificationchoice == 6:
            studentList[studToModify].email = str(updatedvalue)
            moderator.DisplayRecords(studentList[studToModify])

        else:
            studentList[studToModify].home = str(
                updatedvalue)  # Since validation is already done, final record left is home therefore else is used instead of elif
            moderator.DisplayRecords(studentList[studToModify])

    def DeleteRecord(self, emailaddress):  # Function to delete student records
        studToDelete = moderator.SearchRecord(emailaddress)  # Search is done by email address
        del studentList[studToDelete]

    def ViewRegistered(self):  # Displays all available,registered students in the list
        for i in range(self.studentList.__len__()):  # By checking a date of registration exists
            if studentList[i].dor is not None:
                return i


studentObject = student('', '', '', '', '', '', '')  # Create an object instance for student class
moderator = Admin('', '', '', '', '', '', '')  # Creating a moderator object for M class

for i in [5, 4, 3, 2, 1, 0]:
    username = input("Please input your username:\n")
    password = input("Please input your password:\n")  # Admin verification code block with only five attempts
    if moderator.Verification(username, password) == True:
        print("Welcome Admin;\n")
        while True:  # Start of while loop
            print("Select an option to continue..")
            userOption = input(
                "\n a.Add record\n b.Search record\n c.Delete record\n d.View record\n e.Change password\n f.Modify record\n g.Exit application\n").lower()  # Get input of user to proceed with one of the following actions

            if userOption == 'a' or userOption == 'add record':
                detail1 = input("Enter students first name")
                detail2 = input("Enter students surname")
                detail3 = input("Enter students department name")
                detail4 = input("Enter students date of registration")
                detail5 = input("Enter students mobile number")
                detail6 = input("Enter students email address")
                detail7 = input("Enter students home address")
                moderator.AddRecord(detail1, detail2, detail3, detail4, detail5, detail6,
                                    detail7)  # Adds inputted details using the AddRecord function

                print("Students' details have been added to the records.")
                continue

            elif userOption == 'b' or userOption == 'search record':
                studentToSearch = input("Enter students surname to search")
                for i in range(studentList.__len__()):  # Check if student record is in the system
                    if studentList[i].surname == studentToSearch: # if the student in the system execute the function
                          studentSearch = moderator.SearchRecord(
                                          studentToSearch)# Searches students' records using inputted surname;
                          print(f"Here is what was found on {studentToSearch} :\n")
                          moderator.DisplayRecords(
                                                    studentList[studentSearch])  # Then displays students records using the DisplayRecords function
                          break
                else:
                    print("Your request cannot be completed.\nStudent is not in the system")



            elif userOption == 'c' or userOption == 'delete record':
                studentToDelete = input("Enter student email to delete")
                for i in range(studentList.__len__()): # Check if student record is in the system
                    if studentList[i].email == studentToDelete:
                        moderator.DeleteRecord(studentToDelete)  # Deletes students record and prints updated students list
                        print(f"{studentToDelete} Record has been deleted.\n")
                        break
                    else:
                        print("Your request cannot be completed.\nStudent is not in the system")
                        break


            elif userOption == 'd' or userOption == 'view record':
                print("Here is the list of all the registered students:\n")
                for i in range(
                        studentList.__len__()):  # Iterates through the student list and displays all registered students
                    moderator.DisplayRecords(studentList[i])
                continue

            elif userOption == "e" or userOption == 'change password':
                for i in [3, 2, 1, 0]:
                    oldPassword = input("please input old password:\n")
                    if oldPassword == moderator.password:  # Asks to input old password and validates it
                        newPassword = input(
                            "please input new password\n")  # Then asks to input new password and changes it
                        moderator.changePassword(newPassword)
                        print(f"Password has been successfully changed\nyour new password is: {newPassword}")
                        break
                    else:
                        print("Your old password is wrong try again")
                        print(f"you have {i} attempt left")
                        continue

            elif userOption == 'f' or userOption == 'modify record':
                a=True
                studentToModify = input("Enter the students email to modify their record.")

                for i in range(studentList.__len__()): # Check if student record is in the system
                    if studentList[i].email == studentToModify: # if the student in the system execute the function
                        while a: # loop to allow the user to modify more than once or exit
                            ModificationOption = int(input(
                                "Which record would you like to modify?\n 1.First name\n 2.Surname\n 3.Department name\n 4.Date of Registration\n 5.Mobile number\n 6.Email address\n 7.Home address\n 8.Exit "))
                            # Check what exactly is Admin trying to modify
                            if ModificationOption == 1 :
                                newStudentName = input("Enter the students updated first name")
                                print("Here is the updated students records:")
                                moderator.ModifyRecord(studentToModify, ModificationOption,
                                                       newStudentName)  # Ask admin to input new details then modify it using the ModifyRecord function
                                continue

                            elif ModificationOption == 2:
                                newStudentSurname = input("Enter the students updated surname")
                                print("Here is the updated students records:")
                                moderator.ModifyRecord(studentToModify, ModificationOption, newStudentSurname)
                                continue

                            elif ModificationOption == 3:
                                newStudentDepartmentName = input("Enter the students updated department name")
                                print("Here is the updated students records:")
                                moderator.ModifyRecord(studentToModify, ModificationOption, newStudentDepartmentName)
                                continue

                            elif ModificationOption == 4:
                                newStudentDor = input("Enter the students updated date of registration")
                                print("Here is the updated students records:")
                                moderator.ModifyRecord(studentToModify, ModificationOption, newStudentDor)
                                continue

                            elif ModificationOption == 5:
                                newStudentMobileNumber = input("Enter the students updated mobile number")
                                print("Here is the updated students records:")
                                moderator.ModifyRecord(studentToModify, ModificationOption, newStudentMobileNumber)
                                continue

                            elif ModificationOption == 6:
                                newStudentEmail = input("Enter the students updated email address")
                                print("Here is the updated students records:")
                                moderator.ModifyRecord(studentToModify, ModificationOption, newStudentEmail)
                                continue

                            elif ModificationOption == 7:
                                newStudentHomeAddress = input("Enter the students updated home address")
                                print("Here is the updated students records:")
                                moderator.ModifyRecord(studentToModify, ModificationOption, newStudentHomeAddress)
                                continue

                            elif ModificationOption == 8:
                                a = False

                            else:
                                print("Invalid choice, please select a number from 1-7.")
                                continue

                    else:
                        print("Your request cannot be completed.\nStudent is not in the system")


            elif userOption == 'g' or userOption == 'exit application':
                quit()  # Exits/Quits console if users' choice is to exit

            else:
                print(
                    "Invalid option! Select either an alphabet or enter the exact wordings.")  # Continue the loop if users' choice is an invalid option
                continue

    else:  # Else admin authentication handling
        print("Username or password is incorrect, please try again.")
        print(f"you have {i} attempt left..")
        continue
