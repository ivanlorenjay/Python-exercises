# Suma de Dígitos: Escribe una función que tome un número entero y devuelva la suma de sus dígitos. 
# Por ejemplo, para el número 123, la suma sería 1 + 2 + 3 = 6.

def suma_digitos(numero):
    suma = 0
    numero_str = str(numero)

    for digito in numero_str:
        suma += int(digito)

    return suma

try:
    numero_ingresado = int(input("Ingresa un número entero: "))
    resultado = suma_digitos(numero_ingresado)
    print("La suma de los dígitos es:", resultado)
except ValueError:
    print("Error: Ingresaste un valor no válido para un número entero.")
