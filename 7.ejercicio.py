#Imprimir los primeros 10 términos de la serie de Fibonacci usando bucles.
a = 0
b = 1
for i in range (8):
    c = a+b
    a = b
    b = c
print(c)
