numero = int(input("ingrese el numero al cual quiere su factorial"))
factorial = 1
while numero > 1:
    factorial *= numero
    numero -= 1
    print (factorial)
    print (numero)

# Imprimir el resultado
print("El factorial es:", factorial)