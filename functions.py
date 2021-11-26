from os import system  # Will be used to clean screen
#   Student Functions

def listStudents(students):
    print("Listed Students: ")

    for student in students:
        print("Identification: {0} Name: {1} Home Address: {2} Study Address: {3} Email {4} Request Status: {5}\n".format(student[0],student[1],student[2],student[3],student[4],student[5]))


def registerStudent():
    name = input("Student Name: ")
    homeAddress = input("Home Address: ")
    studyAddress = input("Study Address: ")
    email = input("Student's eMail: ")
    regStatus = "Pending"

    student = (name, homeAddress, studyAddress, email, regStatus)
    return student


def existsStudent(students, idStudent):
    exist = False
    for std in students:
        if std[0] == idStudent:
            exist = True
            break
    return exist


def updateStudent():
    name = input("Student Name: ")
    homeAddress = input("Home Address: ")
    studyAddress = input("Study Address: ")
    email = input("Student's eMail: ")
    regStatus = input("Student Status: ")

    if studyAddress == "":
        studyAddress = 'NULL'
    student = (name, homeAddress, studyAddress, email, regStatus)
    return student

#   Course Functions


def listCourses(courses):
    print("Listed Courses: ")

    for course in courses:
        print("CourseId: {0} Name: {1} Credits: {2} Status: {3} \n".format(course[0], course[1], course[2], course[3]))


def registerCourse():
    idCourse = input("Course Acronym: ")
    name = input("Course Name: ")
    totalCredits = input("Credits: ")
    status = input("Status: ")

    course = (idCourse.upper(), name, totalCredits, status)  # Upper idCourse to standardize different idCourses
    return course


def existsCourse(courses, idCourse):
    exist = False
    for crs in courses:
        if crs[0] == idCourse:
            exist = True
            break
    return exist

#   Group Functions


def listGroup(groups):
    print("Listed Groups: ")

    for group in groups:
        print("CourseId: {0} Number: {1}\n".format(group[0], group[1]))


def registerGroup():
    idCourse = checkInput("Course Acronym: ", "String")
    number = checkInput("Group Number: ", "Integer")

    group = (idCourse.upper(), number)  # Upper idCourse to standardize different idCourses
    return group


def existsGroup(groups, groupNumber):
    exist = False
    for gps in groups:
        if gps[1] == int(groupNumber):
            exist = True
            break
    return exist

#   Association President Functions

# True if there is another student in the same year


def existAssociationPresidentInYear(asoPresidents, year):
    exist = False
    for prs in asoPresidents:
        if prs[1] == int(year):
            exist = True
            break
    return exist


#   Period Functions


def listPeriods(periods):
    print("Listed Periods: ")

    for period in periods:
        print("CourseId: {0} Period: {1}\n".format(period[0], period[1]))


def registerPeriod():
    idCourse = checkInput("IdCourse: ", "String")
    period = checkInput("Period: ", "String")


    period = (idCourse.upper(), period)  # Upper idCourse to standardize different idCourses
    return period


def checkInput(text, format):
    while True:
        if format == "String":
            variable = input(text)
            if not variable == "":
                return variable
        if format == "Integer":
            variable = input(text)
            if not variable == "" and variable.isnumeric():
                return int(variable)
        input("Please write a valid input. Try again \nPress enter to continue...")
        system("cls")


def existPeriod(periods, period):
    exist = False
    for prd in periods:
        if prd[0] == period[0] and prd[1] == period[1]:
            exist = True
            break
    return exist


#   Telephone Number Queries

def listPhones(telephones, students):
    print("Listed Phone Numbers")

    for std in students:
        for phone in telephones:
            if int(std[0]) == int(phone[0]):
                print("Student Name: {0} IdStudent {1} Telephone Number: {2}".format(std[1], phone[0], phone[1]))


def existTelephone(telephones, telephone):
    exist = False
    for phones in telephone:
        if phones[0] == telephone[0] and phones[1] == telephone[1]:
            exist = True
            break
    return exist


# StudentGroup Functions

def listStudentEnroll(students,courses, studentGroups):
    print("Listed Enrolled Students Numbers")

    for stdg in studentGroups:
        for crs in courses:
            for std in students:
                if stdg[1] == crs[0] and std[0] == stdg[0]:
                    print("Student Name: {0} Course Name {1} Group Number: {2}".format(std[1], crs[1], stdg[2]))
                    input("Press enter to continue...")


def registerStudentGroup():
    print("Information about student")
    idStudent = int(input("Write student's id: "))
    idCourse = input("IdCourse: ")
    groupNumber = int(input("Write the group: "))

    studentGroup = (idStudent, idCourse.upper(), groupNumber)
    return studentGroup


def existStudentGroup(studentGroups, studentGroup):
    exist = False
    for stdg in studentGroups:
        if stdg[0] == studentGroup[0] and stdg[1] == studentGroup[1] and stdg[2] == studentGroup[2]:
            exist = True
            break
    return exist