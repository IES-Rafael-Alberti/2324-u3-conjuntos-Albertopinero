from src.ejercicio1 import obtener_direcciones 

def test_obtener_direcciones():
        compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
        resultado = {"Calle Las Flores 355", "Mirasol 218", "La Mancha 761"}
        direcciones = obtener_direcciones(compras)
        assert direcciones == resultado