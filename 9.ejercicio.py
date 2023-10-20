# Simular un juego de adivinanza. Genera un número aleatorio entre 1 y 100 y permite al usuario adivinarlo. Proporciona pistas como "Demasiado bajo" o "Demasiado alto" según corresponda.
import random
numero_a_adivinar = random.randint(1,100)
print(numero_a_adivinar)
numeroPuesto=int(input("adivina el numero"))
if numero_a_adivinar == numeroPuesto:
     print("adivinaste su numero es el mismo")
while numero_a_adivinar != numeroPuesto:
  if numeroPuesto > numero_a_adivinar :
     numeroPuesto=int(input("se paso por mas de: ", numero_a_adivinar-numeroPuesto))
  elif numeroPuesto < numero_a_adivinar :
     numeroPuesto=int(input("le falto poco de: ", numero_a_adivinar-numeroPuesto))
  elif numero_a_adivinar == numeroPuesto:
     print("adivinaste su num0ero es el mismo")

