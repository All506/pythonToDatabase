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

