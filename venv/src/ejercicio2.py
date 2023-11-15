'''Ejercicio 3.3.2
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. 
A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.'''

def listar_nombres_primaria_y_secundaria():
    nombres_primaria = []

    # Aquí se solicitan los nombres de primaria hasta ingresar x para finalizar
    nombre = input("Introduce el nombre de un alumno de primaria (o 'x' para finalizar): ")
    while nombre.lower() != "x":
        nombres_primaria.append(nombre)
        nombre = input("Introduce el nombre de un alumno de primaria (o 'x' para finalizar): ")

    nombres_secundaria = []

    # Aquí se solicitan los nombres de secundaria hasta ingresar x para finalizar
    nombre = input("Introduce el nombre de un alumno de secundaria (o 'x' para finalizar): ")
    while nombre.lower() != "x":
        nombres_secundaria.append(nombre)
        nombre = input("Introduce el nombre de un alumno de secundaria (o 'x' para finalizar): ")

    # Aquí se muestran los nombres de ambos grupos sin repetir ninguno
    todos_los_nombres = set(nombres_primaria + nombres_secundaria)
    print("\nNombres de todos los alumnos sin repeticiones:")
    print(todos_los_nombres)

    # Aquí se muestran los nombres que se repiten en secundaria y primaria
    nombres_repetidos = set(nombres_primaria) & set(nombres_secundaria)
    print("\nNombres que se repiten entre primaria y secundaria:")
    print(nombres_repetidos)

    # Aqui se muestran los nombres de primaria que no se repiten en secundaria
    nombres_primaria_no_repetidos = set(nombres_primaria) - set(nombres_secundaria)
    print("\nNombres de primaria que no se repiten en secundaria:")
    print(nombres_primaria_no_repetidos)

    # Aquí se muestra si todos los nombres de primaria estan incluidos en secundaria con un booleano, es decir, True o False
    todos_en_secundaria = set(nombres_primaria) <= set(nombres_secundaria)
    print("\n¿Todos los nombres de primaria están incluidos en secundaria?")
    print(todos_en_secundaria)

if __name__ == "__main__":
    listar_nombres_primaria_y_secundaria()