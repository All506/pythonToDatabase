class studentGroupQueries:

    # Methods related to studentGroup

    def listStudentGroup(self, conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT IdStudent, IdCourse, GroupNumber FROM tblStudentGroup;")

                studentsGroup = cursor.fetchall()

                return studentsGroup
        except Exception as e:
            print("Error in query: ", e)
        finally:
            conexion.close()


    def registStudentGroup(self, conexion, studentGroup):
        try:
            with conexion.cursor() as cursor:
                    sql = "INSERT INTO tblStudentGroup(IdStudent, IdCourse, GroupNumber) VALUES ('{0}','{1}','{2}')"
                    cursor.execute(sql.format(studentGroup[0], studentGroup[1], studentGroup[2]))
                    conexion.commit()

            print("Student has been enrolled!\n")
        except Exception as e:
            print("Error in register query: ", e)
        finally:
            input()
            conexion.close()


    def deleteStudentGroup(self, conexion, studentGroup):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM tblStudentGroup WHERE IdStudent = '{0}' AND IdCourse = '{1}' AND GroupNumber = '{2}'"
                cursor.execute(sql.format(studentGroup[0],studentGroup[1],studentGroup[2]))
                conexion.commit()
                print("Student has been un enrolled")
        except Exception as e:
            print("Error in deleting query: ", e)
        finally:
            input()
            conexion.close()