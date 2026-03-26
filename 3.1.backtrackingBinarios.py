def generar_binarios(n, cadena=""):
    if len(cadena) == n: #validar si la solución es aceptable
        print(cadena)
        return
    generar_binarios(n, cadena + "1")
    generar_binarios(n, cadena + "0")
# Ejemplo:




    


        
