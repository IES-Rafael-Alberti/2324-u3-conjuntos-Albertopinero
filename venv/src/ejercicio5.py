'''Ejercicio 3.3.5¶
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.'''
def pares_y_multiplos():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares = {numero for numero in numeros if numero % 2 == 0}
    multiplos_de_tres = {numero for numero in numeros if numero % 3 == 0}
    pares_y_multiplos_de_tres = pares.intersection(multiplos_de_tres)
    print("Conjunto de números pares:", pares)
    print("Conjunto de múltiplos de tres:", multiplos_de_tres)
    print("Comunes entre pares y múltiplos de tres:", pares_y_multiplos_de_tres)

if __name__ == "__main__":
    pares_y_multiplos()