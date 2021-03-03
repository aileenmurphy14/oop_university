# CMPT 258 Project 1
#Aileen Murphy and Raziel BenReuben

#Instructor class with attributes instructor ID, name, and affiliated department
class Instructor:
    def __init__(self, ID, name, dept):
        self.__ID = ID
        self.__name = name
        self.__dept = dept

    def get_id(self):
        return self.__ID
    
    def get_name(self):
        return self.__name
    
    def get_dept(self):
        return self.__dept

#Department class with attributes department name, location, and budget
class Department:
    def __init__(self, dept, location, budget):
        self.__dept = dept
        self.__location = location
        self.__budget = budget
    
    def get_dept(self):
        return self.__dept

    def get_location(self):
        return self.__location

    def get_budget(self):
        return self.__budget

#Aileen Murphy
#retrieves each line in the instructor file and creates Instructor object for each
#adds each Instructor object to list of instructors
def readInstructorFile(file):
    instructors = []
    for line in file:
        l = line.strip().split(",")
        ID, name, dept = l[0], l[1], l[2]
        instructors.append(Instructor(ID, name, dept))
    return instructors

#Aileen Murphy
#retrieves each line in the department file and creates Department object for each
#adds each Department object to list of departments
def readDepartmentFile(file):
    departments = []
    for line in file:
        l = line.strip().split(",")
        dept, location, budget = l[0], l[1], l[2]
        departments.append(Department(dept, location, budget))
    return departments

#Aileen Murphy
#displays menu choice for user to choose from and exits if option 5 or invalid choice is chosen.      
def getMenuChoice(instructors, departments):
    end = False
    while end == False:
        print("1. Get instructor information.\
                   \n2. Get department information.\
                   \n3. Insert a new record about a new instructor.\
                   \n4. Delete a record about an instructor.\n5. Exit")
        c = eval(input())
        if c == 1:
            option1(instructors, departments)
        elif c == 2:
            option2(instructors, departments)
        elif c == 3:
            option3(instructors, departments)
        elif c == 4:
            option4(instructors, departments)
        else:
            end = True
            print("\nExiting menu... have a nice day!")

#Raziel BenReuben
#searches list of Instructor objects for matching instructor ID
#displays information of Instructor and corresponding Department if ID exists
def option1(instructors, departments):
    does_exist = False
    instructor_id = input("\nEnter instructor ID: ")
    for instructor in instructors:
        if instructor_id == instructor.get_id():
            for department in departments:
                if department.get_dept() == instructor.get_dept():
                    print("Location:", department.get_location())
                    print("Name:", instructor.get_name())
                    print("Department:", instructor.get_dept(), "\n")
                    does_exist = True
    if not does_exist:
        print("\nThe ID does not appear in the file.\n")

#Raziel BenReuben
#searches list of Department objects for matching department name
#displays location, budget, and names of all instructors that work for department if department exists
def option2(instructors, departments):
    not_present = False
    instructor_dept = input("\nEnter the department name: ")
    for department in departments:
        if instructor_dept == department.get_dept():
            print("\nDepartment:", department.get_location())
            print("Budget:", department.get_budget())
            not_present = True
            print("\nList of Instructors:")
            for instructor in instructors:
                if department.get_dept() == instructor.get_dept():
                    print(instructor.get_name())
            print("\n")
    if not not_present:
        print("The department name does not appear in the file.\n")

#Aileen Murphy
#allows for input from user and writes information to instructor file if the department exists and the instructor ID
#is not already in the file
def option3(instructors, departments):
    instructorId = input("Enter the instructor id: ")
    instructorName = input("Enter the instructor name: ")
    departmentName = input("Enter the affiliated department name: ")
    deptExists, instIdExists = False, False
    for dept in departments:
        if departmentName == dept.get_dept():
            deptExists = True
    if deptExists == False:
        print("The department does not exist and hence the instructor record cannot be added to the database.\n")
    for inst in instructors:
        if instructorId == inst.get_id():
            print("Instructor ID already exists in the file.\n")
            instIdExists = True
    if deptExists == True and instIdExists == False:
        instructorFile = open('/Users/aileenmurphy/Documents/CMPT_258/instructor.txt', 'a')   #appends to end of .txt file
        instructorFile.write("\n" + instructorId + ',' + instructorName + ',' + departmentName)
        instructorFile.close()
        instructors.append(Instructor(instructorId, instructorName, departmentName))
        print("Your record has been stored.\n")

#Aileen Murphy
#allows for input from user to enter instructor ID to delete corresponding information in instructor file
#if the ID already exists in the file.
def option4(instructors, departments):
    idExists = False
    lines=[]
    instructorId = input("\nEnter the instructor ID: ")
    for inst in instructors:
        if instructorId == inst.get_id():
            instructors.remove(inst)
            idExists = True
        else:
            lines.append(inst)           
    if idExists == False:
        print("The ID does not appear in the file.\n")
    else:
        instructorFile = open('/Users/aileenmurphy/Documents/CMPT_258/instructor.txt', 'w')   #writes to .txt file
        for l in lines:
            instructorFile.write(l.get_id() + ',' + l.get_name() + ',' + l.get_dept() + '\n')
        instructorFile.close()
        print("Your record has been deleted.\n")
        
#Aileen Murphy
#main method that reads in instructor and department files and calls menu function       
def main():
    instructorFile = open('/Users/aileenmurphy/Documents/CMPT_258/instructor.txt', 'r')   #reads in instructor file
    instructors = readInstructorFile(instructorFile)
    instructorFile.close()
    departmentFile = open('/Users/aileenmurphy/Documents/CMPT_258/department.txt', 'r')   #reads in department file
    departments = readDepartmentFile(departmentFile)
    departmentFile.close()
    getMenuChoice(instructors, departments)   
main()
