""" /*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */ """


orig = 1_000_000_000
n = orig

b = ''

while n > 0:
    b += str(n % 2)
    n //= 2

# La cadena debe ser invertada para obtener el resultado correcto
b = b[::-1]

print(f"El número {orig} en binario es {b} y debería ser {bin(orig)}")