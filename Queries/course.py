class courseQueries:

    # Methods related to course

    def listCourses(self, conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT IdCourse, Name, Credits, Active FROM tblCourse;")

                cursos = cursor.fetchall()

                return cursos
        except Exception as e:
            print("Error in query: ", e)
        finally:
            conexion.close()


    def registCourse(self, conexion, course):
        try:
            with conexion.cursor() as cursor:
                    sql = "INSERT INTO tblCourse(IdCourse,Name,Credits,Active) VALUES ('{0}','{1}','{2}','{3}')"
                    cursor.execute(sql.format(course[0], course[1], course[2],course[3]))
                    conexion.commit()

            print("Course has been registered!\n")
        except Exception as e:
            print("Error in register query: ", e)
        finally:
            input()
            conexion.close()


    def deleteCourse(self, conexion, courseId):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM tblCourse WHERE IdCourse = '{0}'"
                cursor.execute(sql.format(courseId))
                conexion.commit()
                print("Course have been deleted")
        except Exception as e:
            print("Error in deleting query: ", e)
        finally:
            input()
            conexion.close()

    def updateCourse(self, conexion, course):
        try:
            with conexion.cursor() as cursor:
                sql = "UPDATE tblCourse SET Name = '{0}', Credits = '{1}', Active = '{2}' WHERE IdCourse = '{3}'"
                cursor.execute(sql.format(course[1], course[2], course[3], course[0]))
                conexion.commit()
                print("Course have been updated")
        except Exception as e:
            print("Error in updating query: ", e)
        finally:
            input()
            conexion.close()