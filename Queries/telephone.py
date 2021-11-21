class telephoneQueries:

    # Methods related to telephone numbers

    def listTelephones(self, conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT IdStudent, Telephone FROM tblTelephone")
                telephones = cursor.fetchall()
                return telephones
        except Exception as e:
            print("Error in query: ", e)
        finally:
            conexion.close()


    def registerTelephone(self, conexion, telephone):
        try:
            with conexion.cursor() as cursor:
                    sql = "INSERT INTO tblTelephone(IdStudent,Telephone) VALUES ('{0}','{1}')"
                    cursor.execute(sql.format(telephone[0], telephone[1]))
                    conexion.commit()

            print("Telephone has been registered!\n")
        except Exception as e:
            print("Error in register query: ", e)
        finally:
            input()
            conexion.close()


    def deleteTelephone(self, conexion, telephone):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM tblTelephone WHERE idStudent = {0} and Telephone = {1}"
                cursor.execute(sql.format(telephone[0],telephone[1]))
                conexion.commit()
                print("Telephone have been deleted")
        except Exception as e:
            print("Error in deleting query: ", e)
        finally:
            input()
            conexion.close()
