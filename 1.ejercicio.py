def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def imprimir_primos_entre_rangos(minimo, maximo):
    for num in range(minimo, maximo + 1):
        if es_primo(num):
            print(num)

imprimir_primos_entre_rangos(1, 1000)
