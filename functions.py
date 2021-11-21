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
    idCourse = input("Course Acronym: ")
    number = input("Group Number: ")

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
    idCourse = input("IdCourse of Period: ")
    period = input("Period: ")

    period = (idCourse.upper(), period)  # Upper idCourse to standardize different idCourses
    return period


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