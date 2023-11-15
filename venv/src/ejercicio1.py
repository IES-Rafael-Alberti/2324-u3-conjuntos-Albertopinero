'''Ejercicio 3.3.1 - Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene
tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Escribir una función que reciba como parámetro
una lista con el formato mencionado anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. 
Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que contenga 
cada domicilio una sola vez.'''
def solicita_compras() -> list:
    return [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

def obtener_direcciones(compras: list) -> set:
    direcciones = set()
    for compra in compras:
        direcciones.add(compra[3])
    return direcciones
    
def mostrar_direcciones(direcciones: set):
    contador = 0
    for direccion in direcciones:
        contador = contador + 1
        print(f"Direccion {contador}: {direccion}")


if __name__ == "__main__":
    
    # Entrada
    compras = solicita_compras()

    # Proceso 
    direcciones = obtener_direcciones(compras)

    # Salida
    mostrar_direcciones(direcciones)