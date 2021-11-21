class periodQueries:

    # Methods related to periods

    def listPeriods(self, conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT IdCourse, Period FROM tblPeriod;")

                periods = cursor.fetchall()

                return periods
        except Exception as e:
            print("Error in query: ", e)
        finally:
            conexion.close()


    def registPeriod(self, conexion, period):
        try:
            with conexion.cursor() as cursor:
                    sql = "INSERT INTO tblPeriod(IdCourse,Period) VALUES ('{0}','{1}')"
                    cursor.execute(sql.format(period[0], period[1]))
                    conexion.commit()

            print("Period has been registered!\n")
        except Exception as e:
            print("Error in register query: ", e)
        finally:
            input()
            conexion.close()


    def deletePeriod(self, conexion, period):
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM tblPeriod WHERE IdCourse = '{0}' AND Period = '{1}'"
                cursor.execute(sql.format(period[0], period[1]))
                conexion.commit()
                print("Period have been deleted")
        except Exception as e:
            print("Error in deleting query: ", e)
        finally:
            input()
            conexion.close()
