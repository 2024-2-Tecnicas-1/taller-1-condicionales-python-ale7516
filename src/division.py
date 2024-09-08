def evaluar(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    respuesta = ("La división es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
    if residuo == 0 else
        "La división no es exacta. \n" \
        "Cociente: " + str(cociente) + "\n" \
        "Residuo: " + str(residuo)
    )
    
    return respuesta
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
