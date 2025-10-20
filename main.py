from control import students, grades, helpers

def mostrar_menu():
    print(f"MENÚ DE GESTIÓN DE ALUMNOS\n1. Añadir alumno\n2. Eliminar alumno por ID\n3. Eliminar alumno por nombre\n4. Registrar nota\n5. Ver alumnos\n6. Ver media de la clase\n7. Ver aprobados\n8. Ver suspensos\n9. Salir")


def main():
    alumnos = []
    salir = False

    while not salir:
        mostrar_menu()
        opcion = helpers.pedir_opcion()

        if opcion == 1:
            nombre = helpers.pedir_nombre()
            try:
                print(students.crear_alumno(alumnos, nombre))
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == 2:
            student_id = helpers.pedir_id()
            if student_id is not None:
                try:
                    print(students.borrar_alumno_por_id(alumnos, student_id))
                except Exception as e:
                    print(f"Error: {e}")

        elif opcion == 3:
            nombre = helpers.pedir_nombre()
            try:
                print(students.borrar_alumno_por_nombre(alumnos, nombre))
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == 4:
            student_id = helpers.pedir_id()
            nota = helpers.pedir_nota()
            if student_id is not None and nota is not None:
                try:
                    print(grades.registrar_nota(alumnos, student_id, nota))
                except Exception as e:
                    print(f"Error: {e}")

        elif opcion == 5:
            print(students.ver_alumnos(alumnos))

        elif opcion == 6:
            try:
                print(f"Media de la clase: {grades.media_clase(alumnos):.2f}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == 7:
            print(grades.mostrar_aprobados(alumnos))

        elif opcion == 8:
            print(grades.mostrar_suspensos(alumnos))

        elif opcion == 9:
            print("Saliendo del programa")
            salir = True

        else:
            print("Opción no válida, intenta otra ve.")


if __name__ == "__main__":
    main()
