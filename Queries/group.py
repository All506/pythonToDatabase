class groupQueries:

    # Methods related to group

    def listGroups(self, conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT IdCourse, Number FROM tblGroup;")

                groups = cursor.fetchall()

                return groups
        except Exception as e:
            print("Error in query: ", e)
        finally:
            conexion.close()


    def registGroup(self, conexion, group):
        try:
            with conexion.cursor() as cursor:
                    sql = "INSERT INTO tblGroup(IdCourse,Number) VALUES ('{0}','{1}')"
                    cursor.execute(sql.format(group[0], group[1]))
                    conexion.commit()

            print("Group has been registered!\n")
        except Exception as e:
            print("Error in register query: ", e)
        finally:
            input()
            conexion.close()


    def deleteGroup(self, conexion, groupNumber):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM tblGroup WHERE Number = '{0}'"
                cursor.execute(sql.format(groupNumber))
                conexion.commit()
                print("Course have been deleted")
        except Exception as e:
            print("Error in deleting query: ", e)
        finally:
            input()
            conexion.close()

    def updateGroup(self, conexion, group):
        try:
            with conexion.cursor() as cursor:
                sql = "UPDATE tblGroup SET IdCourse = '{0}' WHERE Number = '{1}'"
                cursor.execute(sql.format(group[0], group[1]))
                conexion.commit()
                print("Group have been updated")
        except Exception as e:
            print("Error in updating query: ", e)
        finally:
            input()
            conexion.close()