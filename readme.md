"""

# Trabajo práctico: gestión de alumnos y calificaciones


Desarrolla un programa en Python que permita gestionar la información de alumnos y sus calificaciones, utilizando funciones, manejo de excepciones y módulos para organizar el código.
El objetivo es simular un sistema sencillo de gestión educativa donde se puedan añadir alumnos, registrar notas, consultar medias y eliminar registros.


## Conocimientos que implementaremos en este trabajo
	- Aplicar los conocimientos de variables, tipos de datos, listas, diccionarios, bucles y condicionales.
	- Implementar y reutilizar funciones correctamente estructuradas.
	- Controlar errores con excepciones (try, except, raise).
	- Organizar el código en módulos para un diseño más profesional.


## Estructura del proyecto

Tu proyecto debe de tener la siguiente estructura (mínimo):
	- StudentManager/
	- - main.py
	- - control/
	- - - students.py
	- - - grades.py
	- - - helpers.py


- Toda la interacción con el usuario (entradas por teclado y salidas por pantalla) se realizará exclusivamente en main.py. 
- Los módulos dentro de control/ expondrán funciones que reciban datos (una lista con diccionarios dentro) y devuelvan resultados o lancen excepciones cuando corresponda. 
- Se trabajará con nombres de variables y funciones. No se permite usar ficheros todavía (sin persistencia en disco).


## Cómo funciona el programa

Cada elemento de la lista será un diccionario con la estructura: {student_id, nombre, nota}

	- El programa debe permitir en gestión de alumnos (Todo esto va en students.py): 
		- gestión de alumnos: Se creará un alumno con el nombre. Este no puede estar vacío, ni puede ser numérico y se creará automáticamente un student_id. Podéis usar la librería random (El id debe de ser único).
		- Función de borrar alumno por id y otra por nombre. Solo puede dejar borrar los alumnos que tengan de nota menos de 5.
		- Ver todos los alumnos que hayan cuya impresión por consola es: {nombre y nota}
	- En grades.py haremos funciones que hagan la media de notas de la clase, otra función para mostrar los suspensos y otra para los aprobados.
	- Los helpers.py los usaremos para introducir contenido por consola y comprobar con try/except los datos introducidos.
	- El archivo main.py es el archivo principal del programa donde tendremos el menú. 

"""
