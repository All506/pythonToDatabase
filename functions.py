def listarCursos(cursos):
    print("Listed Students: ")
    contador = 1

    for students in cursos:
        print("Name: {0} Identification: {1}".format(students[0],students[1]))
