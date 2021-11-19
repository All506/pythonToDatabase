from BD.conexion import DAO
import functions

if __name__ == '__main__':
    dao = DAO()

    try:
        cursos = dao.listarCursos(dao.getConection())
        functions.listarCursos(cursos)
    except:
       print("Error en cursos")



