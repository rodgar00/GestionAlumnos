def input_user_opcion():
    try:
        opcion = int(input("\nElige una opción: "))
        return opcion
    except ValueError:
        print("Debes introducir un número válido.")
        return None


def input_user_nombre():
    nombre = input("Introduce el nombre del alumno: ")
    return nombre


def input_user_id():
    try:
        student_id = int(input("Introduce el ID del alumno: "))
        return student_id
    except ValueError:
        print("El ID debe ser numérico.")
        return None


def input_user_nota():
    try:
        nota = float(input("Introduce la nota (0-10): "))
        return nota
    except ValueError:
        print("La nota debe ser un número válido.")
        return None
