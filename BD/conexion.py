import pyodbc


class DAO:  # Data Access Object

    def getConection(self):
        try:
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                      '163.178.107.10' + ';DATABASE=' + 'Project_C00648_C07870' + ';UID=' + 'laboratorios' + ';PWD=' + 'KmZpo.2796')
            return conexion
        except Exception as ex:
            print("Connection was not established {0}", ex)
        input()