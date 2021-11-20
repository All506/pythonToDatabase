from os import system # Will be used to clean screen
# related to database controllers
from BD.conexion import DAO
import functions
from Queries.student import studentQueries

dao = DAO() # Data Access Object


def mainMenu():
    while True:
        system('cls')
        print("1. Students")
        option = int(input("Please choose one of the options to use "))
        if option == 1:
            studentMenu()


def studentMenu():
    sq = studentQueries()
    while True:
        system('cls')
        print("1. Show all students")
        print("2. Create a new student")
        print("3. Delete all students")
        print("4. Update a student")
        print("5. Go back to Main Menu")
        option = int(input("Please choose one of the options to use "))
        if option>5 or option<=0:   # Invalid Option
            print("Chose one valid option. Please try again...")
            input()
        else:
            if option == 1:  # Show all students
                print("Please hold a sec...")
                students = sq.listStudents(dao.getConection())
                system('cls')
                functions.listStudents(students)
                input()
            elif option == 2:  # Create a new student
                student = functions.registerStudent()
                sq.registStudent(dao.getConection(),student)
            elif option == 3:  # Delete a specific student
                print("Please hold a sec...")
                students = sq.listStudents(dao.getConection())
                system('cls')
                functions.listStudents(students)
                studentId = input("Please write the id to delete: ")
                if functions.existsStudent(students,studentId):
                    sq.deleteStudent(dao.getConection(), studentId)
                else:
                    print("Id does not exist. Please try again")
                    input()
            elif option == 4:   # Update a student
                print("Please hold a sec...")
                students = sq.listStudents(dao.getConection())
                system('cls')
                functions.listStudents(students)
                studentId = int(input("Please write the id to update: "))
                if functions.existsStudent(students, studentId):
                    sq.updateStudent(dao.getConection(), studentId, functions.updateStudent())
                else:
                    print("Id does not exist. Please try again")
                    input()
            elif option == 5:   # Return to main
                break
