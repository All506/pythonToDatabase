from os import system  # Will be used to clean screen
# related to database controllers
from BD.conexion import DAO
import functions
from Queries.student import studentQueries
from Queries.course import courseQueries
from Queries.group import groupQueries
from Queries.asoPresident import asoPresidentQueries
from Queries.period import periodQueries
from Queries.telephone import telephoneQueries
from Queries.studentGroup import studentGroupQueries

dao = DAO()  # Data Access Object


def mainMenu():
    while True:
        system('cls')
        print("1. Students")
        print("2. Courses")
        print("3. Periods")
        print("4. Groups")
        print("5. Enroll Student")
        print("6. Views")
        print("7. Exit")
        option = int(input("Please choose one of the options to use "))
        if option == 1:
            studentMenu()
        elif option == 2:
            courseMenu()
        elif option == 3:
            periodMenu()
        elif option == 4:
            groupMenu()
        elif option == 5:
            enrollMenu()
        elif option == 6:
            viewMenu()
        elif option == 7:
            break
        else:
            system('cls')
            print("Please select a valid option")
            input("Press enter to continue...")

#   Student menu

def studentMenu():
    sq = studentQueries()
    ap = asoPresidentQueries()
    while True:
        system('cls')
        print("1. Show all students")
        print("2. Create a new student")
        print("3. Delete a student")
        print("4. Update a student")
        print("5. Contact Information")
        print("6. Declare Student's Association President")
        print("7. Go back to Main Menu")
        option = int(input("Please choose one of the options to use "))
        if option > 7 or option <= 0:  # Invalid Option
            print("Chose one valid option. Please try again...")
            input("Press enter to continue...")
        else:
            if option == 1:  # Show all students
                print("Please hold a sec...")
                students = sq.listStudents(dao.getConection())
                system('cls')
                functions.listStudents(students)
                input("Press enter to continue...")
            elif option == 2:  # Create a new student
                student = functions.registerStudent()
                sq.registStudent(dao.getConection(), student)
            elif option == 3:  # Delete a specific student
                print("Please hold a sec...")
                students = sq.listStudents(dao.getConection())
                system('cls')
                functions.listStudents(students)
                studentId = input("Please write the id to delete: ")
                if functions.existsStudent(students, studentId):
                    sq.deleteStudent(dao.getConection(), studentId)
                else:
                    print("Id does not exist. Please try again")
                    input("Press enter to continue...")
            elif option == 4:  # Update a student
                print("Please hold a sec...")
                students = sq.listStudents(dao.getConection())
                system('cls')
                functions.listStudents(students)
                studentId = int(input("Please write the id to update: "))
                if functions.existsStudent(students, studentId):
                    sq.updateStudent(dao.getConection(), studentId, functions.updateStudent())
                else:
                    print("Id does not exist. Please try again")
                    input("Press enter to continue...")
            elif option == 5:
                phoneNumberMenu()
            elif option == 6:
                print("Please hold a sec...")
                students = sq.listStudents(dao.getConection())
                asoPresidents = ap.listAsoPresident(dao.getConection())
                system('cls')
                studentId = int(input("Please write student's id to declare Student's President: "))
                if functions.existsStudent(students, studentId):
                    govYear = int(input("What's the goverment year?: "))
                    #   Will check if there is a student registered in this same year
                    if not functions.existAssociationPresidentInYear(asoPresidents,govYear):
                        sq.declarePresident(dao.getConection(),studentId,govYear)
                    else:
                        print("There is a student who ruled this year. \n Try with a different year")
                        input("Press enter to continue...")
                else:
                    print("Id does not exist. Please try again")
                    input("Press enter to continue...")
            elif option == 7:  # Return to main
                break


#   Course Menu

def courseMenu():
    cq = courseQueries()
    while True:
        system('cls')
        print("1. Show all courses")
        print("2. Create a new course")
        print("3. Delete a course")
        print("4. Update a course")
        print("5. Go back to Main Menu")
        option = int(input("Please choose one of the options to use "))
        if option > 5 or option <= 0:  # Invalid Option
            print("Chose one valid option. Please try again...")
            input("Press enter to continue...")
        else:
            if option == 1:  # Show all courses
                print("Please hold a sec...")
                courses = cq.listCourses(dao.getConection())
                system('cls')
                functions.listCourses(courses)
                input("Press enter to continue...")
            elif option == 2:  # Create a new course
                system('cls')
                print("New Course Information")
                courses = functions.registerCourse()
                cq.registCourse(dao.getConection(), courses)
            elif option == 3:  # Delete a specific course
                print("Please hold a sec...")
                courses = cq.listCourses(dao.getConection())
                system('cls')
                functions.listCourses(courses)
                courseId = input("Please write the id to delete: ")
                if functions.existsCourse(courses, courseId):
                    cq.deleteCourse(dao.getConection(), courseId)
                else:
                    print("Id does not exist. Please try again")
                    input("Press enter to continue...")
            elif option == 4:  # Update a course
                print("Please hold a sec...")
                courses = cq.listCourses(dao.getConection())
                system('cls')
                functions.listCourses(courses)
                courseId = input("Please write the id to update: ")
                if functions.existsCourse(courses, courseId):
                    cq.updateCourse(dao.getConection(), functions.registerCourse())
                else:
                    print("Id does not exist. Please try again")
                    input("Press enter to continue...")
            elif option == 5:  # Return to main
                break

#   Group Menu

def groupMenu():
    gq = groupQueries()
    cq = courseQueries()
    while True:
        system('cls')
        print("1. Show all groups")
        print("2. Create a new group")
        print("3. Delete a group")
        print("4. Update a group")
        print("5. Go back to Main Menu")
        option = int(input("Please choose one of the options to use "))
        if option > 5 or option <= 0:  # Invalid Option
            print("Chose one valid option. Please try again...")
            input("Press enter to continue...")
        else:
            if option == 1:  # Show all groups
                print("Please hold a sec...")
                groups = gq.listGroups(dao.getConection())
                system('cls')
                functions.listGroup(groups)
                input("Press enter to continue...")
            elif option == 2:  # Create a new group
                print("Please hold a sec...")
                courses = cq.listCourses(dao.getConection())
                system('cls')
                print("New Group Information")
                group = functions.registerGroup()
                if functions.existsCourse(courses, group[0]):
                    gq.registGroup(dao.getConection(), group)
                else:
                    print("Course is not registered. Please try again...")
                    input("Press enter to continue...")
            elif option == 3:  # Delete a specific group by number
                print("Please hold a sec...")
                groups = gq.listGroups(dao.getConection())
                system('cls')
                functions.listGroup(groups)
                number = input("Please write the group number to delete: ")
                if functions.existsGroup(groups, number):   # Will make sure courseId exists
                    gq.deleteGroup(dao.getConection(), number)
                else:
                    print("Id does not exist. Please try again")
                    input("Press enter to continue...")
            elif option == 4:  # Update a group
                print("Please hold a sec...")
                courses = cq.listCourses(dao.getConection())
                groups = gq.listGroups(dao.getConection())
                system('cls')
                functions.listGroup(groups)
                groupNumber = input("Please write group number to update: ")
                if functions.existsGroup(groups, groupNumber):
                    idCourse = input("Write new idCourse for group: ")
                    idCourse.upper()    #   Will convert to uppercase
                    if functions.existsCourse(courses, idCourse):
                        group = (idCourse, groupNumber)
                        gq.updateGroup(dao.getConection(), group)
                    else:
                        print("Course is not registered. Please try again...")
                        input("Press enter to continue...")

                else:
                    print("Id does not exist. Please try again")
                    input("Press enter to continue...")
            elif option == 5:  # Return to main
                break

# Period Queries There is not update option. Basically 'cause there is nothing you can update. IdCourse or Period,
# and how you will check? By period or idCourse when both can be specific arguments to look up


def periodMenu():
    pq = periodQueries()
    cq = courseQueries()
    while True:
        system('cls')
        print("1. Show all periods")
        print("2. Create a new period")
        print("3. Delete a period")
        print("4. Go back to Main Menu")
        option = int(input("Please choose one of the options to use "))
        if option > 4 or option <= 0:  # Invalid Option
            print("Chose one valid option. Please try again...")
            input()
        else:
            if option == 1:  # Show all periods
                print("Please hold a sec...")
                periods = pq.listPeriods(dao.getConection())
                system('cls')
                functions.listPeriods(periods)
                input("Press enter to continue...")
            elif option == 2:  # Create a new period
                print("Please hold a sec...")
                courses = cq.listCourses(dao.getConection())
                system('cls')
                print("New Period Information")
                periods = functions.registerPeriod()
                if functions.existsCourse(courses, periods[0]):
                    pq.registPeriod(dao.getConection(), periods)
                else:
                    print("There is no course registered by that id")
                    input("Press enter to continue...")
            elif option == 3:  # Delete a specific period
                print("Please hold a sec...")
                periods = pq.listPeriods(dao.getConection())
                system('cls')
                functions.listPeriods(periods)
                period = functions.registerPeriod()
                if functions.existPeriod(periods, period):
                    pq.deletePeriod(dao.getConection(), period)
                else:
                    print("Period is already register. Please try again")
                    input("Press enter to continue...")
            elif option == 4:  # Return to main
                break

#   Contact Number information related to students
def phoneNumberMenu():
    tq = telephoneQueries()
    sq = studentQueries()
    while True:
        system('cls')
        print("Phone Numbers")
        print("1. List all phone numbers")
        print("2. Add a new phone")
        print("3. Delete a phone number")
        print("4. Update a phone number")
        print("5. Return to main menu")
        option = int(input("Select a valid option"))
        if option > 5 or option <= 0:
            print("Selected option is not valid")
            input("Press enter to continue")
        elif option == 1:
            print("Please hold a sec...")
            phones = tq.listTelephones(dao.getConection())
            students = sq.listStudents(dao.getConection())
            system('cls')
            functions.listPhones(phones, students)
            input("Press enter to continue...")
        elif option == 2:
            print("Please hold a sec...")
            students = sq.listStudents(dao.getConection())
            system('cls')
            functions.listStudents(students)
            idStudent = int(input("Write student's id: "))
            if functions.existsStudent(students,idStudent):
                number = input("Write students phone number: ")
                telephone = (idStudent, number)
                tq.registerTelephone(dao.getConection(), telephone)
            else:
                print("Written Student Id does not exist \n Please try again")
                input("Press any key to continue...")
        elif option == 3:
            print("Please hold a sec...")
            telephones = tq.listTelephones(dao.getConection())
            students = sq.listStudents(dao.getConection())
            system('cls')
            functions.listPhones(telephones,students)
            print("Telephone to delete information")
            idStudent = int(input("Write student's id: "))
            system('cls')
            if functions.existsStudent(students, idStudent):
                number = input("Write students phone number: ")
                telephone = (idStudent, number)
                tq.deleteTelephone(dao.getConection(), telephone)
            else:
                print("Written Student Id does not exist \n Please try again")
                input("Press any key to continue...")
        elif option == 4:
            print("Please hold a sec...")
            telephones = tq.listTelephones(dao.getConection())
            students = sq.listStudents(dao.getConection())
            functions.listPhones(telephones,students)
            print("Telephone to update information")
            idStudent = int(input("Write student's id: "))
            system('cls')
            if functions.existsStudent(students, idStudent):
                oldNumber = input("Write students phone number: ")
                # telephone = (idStudent, oldNumber)
                newTelephone = input("Write the new phone number: ")
                tq.deleteTelephone(dao.getConection(), (idStudent, oldNumber))
                tq.registerTelephone(dao.getConection(), (idStudent, newTelephone))
        elif option == 5:
            break;


def enrollMenu():
    stdg = studentGroupQueries()
    cq = courseQueries()
    sq = studentQueries()
    gq = groupQueries()
    while True:
        system('cls')
        print("Enroll Student Menu")
        print("1. Show Enrolled Students")
        print("2. Enroll Student")
        print("3. De-Enroll Student")
        print("4. Return to main menu")
        option = int(input("Select a valid option"))
        if option > 4 or option <= 0:
            print("Select a valid option")
            input("Press enter to continue")
        elif option == 1:
            system('cls')
            print("Please hold a sec...")
            students = sq.listStudents(dao.getConection())
            courses = cq.listCourses(dao.getConection())
            stgroups = stdg.listStudentGroup(dao.getConection())
            system('cls')
            functions.listStudentEnroll(students,courses,stgroups)
        elif option == 2:
            # Make sure group and course exist
            print("Please hold a sec...")
            students = sq.listStudents(dao.getConection())
            courses = cq.listCourses(dao.getConection())
            groups = gq.listGroups(dao.getConection())
            studentGroups = stdg.listStudentGroup(dao.getConection())
            system("cls")
            studentGroup = functions.registerStudentGroup()
            system('cls')
            if functions.existsCourse(courses, studentGroup[1]):
                if functions.existsStudent(students, int(studentGroup[0])):
                    if functions.existsGroup(groups, int(studentGroup[2])):
                        if not functions.existStudentGroup(studentGroups, studentGroup):
                            stdg.registStudentGroup(dao.getConection(), studentGroup)
                        else:
                            print("Student is already registered in same group")
                    else:
                        print("Group is not registered. Please try again...")
                else:
                    print("Student is not registered. Please try again...")
            else:
                print("Course is not registered. Please try again...")
            input("Press enter to continue...")
        if option == 3:
            # Make sure group and course exist
            print("Please hold a sec...")
            studentGroups = stdg.listStudentGroup(dao.getConection())
            system("cls")
            studentGroup = functions.registerStudentGroup()
            system("cls")
            if functions.existStudentGroup(studentGroups, studentGroup):
                stdg.deleteStudentGroup(dao.getConection(), studentGroup)
                input("Press enter to continue")
            else:
                print("Student is not registered in this group")
        if option == 4:
            break


def viewMenu():
    sq = studentQueries()
    while True:
        system('cls')
        print("View Menu")
        print("1. Student and Groups View")
        print("2. Continue")
        option = int(input("Select a valid option"))
        if option > 1 or option < 0:
            print("Select a valid option")
            input("Press enter to continue")
        elif option == 1:
            system('cls')
            sq.showView1(dao.getConection())
            input("Press enter to continue")
        elif option == 2:
            break
