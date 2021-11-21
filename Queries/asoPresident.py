class asoPresidentQueries:
    #   Will enlist all students who have been Association's President
    def listAsoPresident(self, conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT IdStudent, GovYear FROM tblAsoPresident;")

                asoPresident = cursor.fetchall()

                return asoPresident
        except Exception as e:
            print("Error in query: ", e)
        finally:
            conexion.close()
