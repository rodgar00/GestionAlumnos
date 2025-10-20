def registrar_nota(alumnos, student_id, nota):
    if nota < 0 or nota > 10:
        raise ValueError("La nota debe estar entre 0 y 10.")
    for alumno in alumnos:
        if alumno["student_id"] == student_id:
            alumno["nota"] = nota
            return f"Nota registrada para {alumno['nombre']}."
    raise ValueError("No se encontró ningún alumno con ese ID.")


def media_clase(alumnos):
    notas = []
    for alum in alumnos:
        if alum["nota"] is not None:
            notas.append(alum["nota"])
    if len(notas) == 0:
        raise ValueError("No hay notas registradas.")
    suma = 0
    for n in notas:
        suma += n
    return suma / len(notas)


def mostrar_aprobados(alumnos):
    texto = ""
    hay_aprobados = False
    for alum in alumnos:
        if alum["nota"] is not None and alum["nota"] >= 5:
            texto += f"{alum['nombre']} - {alum['nota']}\n"
            hay_aprobados = True
    if not hay_aprobados:
        return "No hay aprobados."
    return texto


def mostrar_suspensos(alumnos):
    texto = ""
    hay_suspensos = False
    for alum in alumnos:
        if alum["nota"] is not None and alum["nota"] < 5:
            texto += f"{alum['nombre']} - {alum['nota']}\n"
            hay_suspensos = True
    if not hay_suspensos:
        return "No hay suspensos."
    return texto
