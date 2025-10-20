import random

def generar_id_unico(alumnos):
    ids_existentes = []
    for a in alumnos:
        ids_existentes.append(a["student_id"])
    nuevo_id = random.randint(1000, 9999)
    while nuevo_id in ids_existentes:
        nuevo_id = random.randint(1000, 9999)
    return nuevo_id


def crear_alumno(alumnos, nombre):
    if not nombre or nombre.isdigit():
        raise ValueError("El nombre no puede estar vacío ni ser un número.")
    nuevo_id = generar_id_unico(alumnos)
    nuevo_alumno = {
        "student_id": nuevo_id,
        "nombre": nombre,
        "nota": None
    }
    alumnos.append(nuevo_alumno)
    return f"Alumno '{nombre}' con ID {nuevo_id} creado."


def borrar_alumno_por_id(alumnos, student_id):
    for alumno in alumnos:
        if alumno["student_id"] == student_id:
            if alumno["nota"] is not None and alumno["nota"] >= 5:
                raise ValueError("Solo puedes borrar alumnos con nota menor a 5.")
            alumnos.remove(alumno)
            return f"Alumno con ID {student_id} eliminado."
    raise ValueError("No hay ningún alumno con ese ID.")


def borrar_alumno_por_nombre(alumnos, nombre):
    for alumno in alumnos:
        if alumno["nombre"].lower() == nombre.lower():
            if alumno["nota"] is not None and alumno["nota"] >= 5:
                raise ValueError("Solo se pueden borrar alumnos con nota inferior a 5.")
            alumnos.remove(alumno)
            return f"Alumno '{nombre}' eliminado."
    raise ValueError("No hay ningún alumno con ese nombre.")


def ver_alumnos(alumnos):
    if len(alumnos) == 0:
        return "No hay alumnos registrados."

    texto = ""
    for alumno in alumnos:
        if alumno["nota"] is None:
            texto += f"{alumno['nombre']} - Nota: Sin nota. ID - {alumno['student_id']}\n"
        else:
            texto += f"{alumno['nombre']} - Nota: {alumno['nota']}. ID - {alumno['student_id']}\n"
    return texto
