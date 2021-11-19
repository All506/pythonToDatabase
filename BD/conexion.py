import pyodbc


class DAO():

    def getConection(self):
        try:
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                      '163.178.107.10' + ';DATABASE=' + 'IF4100DatabaseC00648' + ';UID=' + 'laboratorios' + ';PWD=' + 'KmZpo.2796')
            return conexion
        except Exception as ex:
            print("Error al intentar conexion {0}", ex)


    def listarCursos(self, conexion):
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT name, id  FROM Student;")

                    students = cursor.fetchall()

                    return students
            except Exception as e:
                print("Ocurrió un error al consultar: ", e)
            finally:
                conexion.close()