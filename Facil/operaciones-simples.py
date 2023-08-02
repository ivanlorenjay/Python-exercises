# ingresa un valor flotante para la variable a aquí
a = float(input("Ingresa a: "))
# ingresa un valor flotante para la variable b aquí
b = float(input("Ingresa b: "))

# mostrar el resultado de la suma aquí
print("El resultado de la suma es " + str( a + b ))
# mostrar el resultado de la resta aquí
print("El resultado de la resta es " + str( a - b ))
# mostrar el resultado de la multiplicación aquí
print("El resultado de la multiplicación es",( a * b ))
# mostrar el resultado de la división aquí
print("El resultado de la división es", ( a / b ))

print("\n¡Eso es todo, amigos!")

"""
La función str() en Python se utiliza para convertir un valor en su representación en forma 
de cadena de caracteres. Puedes utilizar la función str() en los siguientes casos:

1.- Convertir números en cadenas de caracteres: Puedes utilizar str() para convertir números 
en su representación en forma de cadena. Por ejemplo, si tienes un número entero x, puedes 
convertirlo en una cadena utilizando str(x).

2.- Concatenar cadenas de caracteres: Puedes utilizar str() para convertir valores en cadenas y luego 
concatenarlas. Por ejemplo, si tienes una variable nombre que contiene un nombre y una variable edad 
que contiene una edad, puedes concatenarlas utilizando str(nombre) + " tiene " + str(edad) + " años".

3.- Imprimir valores junto con texto: Puedes utilizar str() para convertir valores en cadenas y luego 
imprimirlos junto con texto. Por ejemplo, si quieres imprimir el valor de una variable x junto con un
mensaje, puedes utilizar print("El valor de x es: " + str(x)).

Recuerda que la función str() solo puede convertir valores en su representación en forma de cadena de 
caracteres. Si intentas utilizarla en un objeto que no puede ser convertido en una cadena, se producirá un error.
"""