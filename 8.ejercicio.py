#Pedir al usuario que ingrese una serie de números. Calcular y mostrar el promedio de los números ingresados.

guardado = 0
while True:
    contador = 0
    contador =+1
    numero = int(input("agrege un numero"))
    guardado = numero + guardado
    respuesta = input("¿desea seguir agregando numeros?")
    if respuesta == "no":
        promedio = guardado / contador
        print("su promedio guardado de numero es de: " , promedio)
        break
