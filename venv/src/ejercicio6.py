'''Ejercicio 3.3.6
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
'''
def letras_alfabeto():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    consonantes = alfabeto - vocales
    letras_comunes = vocales.intersection(consonantes)
    print("Conjunto de consonantes:", consonantes)
    print("Conjunto de letras comunes:", letras_comunes)

if __name__ == "__main":
    letras_alfabeto()
