class studentQueries:

    # Methods related to students

    def listStudents(self, conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT IdStudent, Name, HomeAddress, StudyAddress, Email, RegStatus  FROM tblStudent;")

                students = cursor.fetchall()

                return students
        except Exception as e:
            print("Error in query: ", e)
        finally:
            conexion.close()

    def registStudent(self, conexion, student):
        try:
            with conexion.cursor() as cursor:
                if student[2] == "":  # Student has one address
                    sql = "INSERT INTO tblStudent(Name,HomeAddress,Email,RegStatus) VALUES ('{0}','{1}','{2}','{3}')"
                    cursor.execute(sql.format(student[0], student[1], student[3], student[4]))
                    conexion.commit()
                else:  # Home address and student address are different
                    sql = "INSERT INTO tblStudent(Name,HomeAddress,StudyAddress,Email,RegStatus) VALUES ('{0}','{1}','{2}','{3}','{4}')"
                    cursor.execute(sql.format(student[0], student[1], student[2], student[3], student[4]))
                    conexion.commit()

            print("Student has been registered!\n")
        except Exception as e:
            print("Error in register query: ", e)
        finally:
            input()
            conexion.close()

    def deleteStudent(self, conexion, studentId):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM tblStudent WHERE IdStudent = '{0}'"
                cursor.execute(sql.format(studentId))
                conexion.commit()
                print("Student have been deleted")
        except Exception as e:
            print("Error in deleting query: ", e)
        finally:
            input()
            conexion.close()

    def updateStudent(self, conexion, studentId, student):
        try:
            with conexion.cursor() as cursor:
                sql = "UPDATE tblStudent SET Name = '{0}', HomeAddress = '{1}', StudyAddress = '{2}', Email = '{3}', RegStatus = '{4}' WHERE IdStudent = '{5}'"
                cursor.execute(sql.format(student[0], student[1], student[2], student[3], student[4], studentId))
                conexion.commit()
                print("Student have been updated")
        except Exception as e:
            print("Error in updating query: ", e)
        finally:
            input()
            conexion.close()

    def declarePresident(self, conexion, studentID, govYear):
        try:
            with conexion.cursor() as cursor:
                    sql = "INSERT INTO tblAsoPresident(IdStudent,GovYear) VALUES ('{0}','{1}')"
                    cursor.execute(sql.format(studentID, govYear))
                    conexion.commit()
                    getName = "SELECT [Name] FROM tblStudent WHERE IdStudent = {0}"
                    cursor.execute(getName.format(studentID))
                    student = cursor.fetchall()
                    conexion.commit()
            print(" {0} has been declared president!\n".format((student[0])[0]))
        except Exception as e:
            print("Error in register query: ", e)
        finally:
            input()
            conexion.close()