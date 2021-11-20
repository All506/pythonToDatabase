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
