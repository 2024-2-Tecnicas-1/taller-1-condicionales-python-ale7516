def evaluar(num_victorias_a, num_victorias_b):
    if num_victorias_a - num_victorias_b == 6:
        return "Ganó A"
    if num_victorias_b - num_victorias_a == 6:
        return "Ganó B"
    if num_victorias_a == 7 and num_victorias_b == 6:
        return "Ganó A"
    if num_victorias_a == 6 and num_victorias_b == 7:
        return "Ganó B"
    if num_victorias_a == 5 and num_victorias_b == 5:
        if num_victorias_a == 7 or num_victorias_b == 7:
            return f"Resultado final: {max(num_victorias_a, num_victorias_b)}-6"
    if num_victorias_a >= 8 or num_victorias_b >= 8:
        return "Inválido"
    if num_victorias_a >= 6 and num_victorias_a - num_victorias_b == 2:
        return "Ganó A"
    if num_victorias_b >= 6 and num_victorias_b - num_victorias_a == 2:
        return "Ganó B"
    if abs(num_victorias_a - num_victorias_b) >= 3:
        return "Inválido"
    
    return "Aún no termina"

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
