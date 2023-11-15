'''Ejercicio 3.3.3
El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» 
(la lista de todos sus subconjuntos):

>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]'''

def conjunto_potencia(conjunto):
    if not conjunto:
        return [set()]
    
    elemento = next(iter(conjunto))
    resto = conjunto - {elemento}
    
    subconjuntos_sin_elemento = conjunto_potencia(resto)
    subconjuntos_con_elemento = [conjunto.union({elemento}) for conjunto in subconjuntos_sin_elemento]
    
    return subconjuntos_sin_elemento + subconjuntos_con_elemento

if __name__ == "__main__":
    conjunto_ejemplo = {1, 2, 3}
    resultado = conjunto_potencia(conjunto_ejemplo)
    print(resultado)
