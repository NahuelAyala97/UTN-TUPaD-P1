'''1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario'''

def factorial(num):
    if num == 0:
       return 1
    return factorial(num-1) * num

num_int = int(input("Ingrese un número entero: "))

for n in range(1, num_int + 1):
    print(f'Factorial de {n}: {factorial(n)}\b')


'''2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.'''

def secuencia_fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return secuencia_fibonacci(num - 1) + secuencia_fibonacci(num - 2)

num_int = int(input("Ingrese un número entero: "))

for n in range(1, num_int + 1):
    print(f'Secuencia de fibonacci hasta el {n}: {secuencia_fibonacci(n)}\b')


'''3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n**m = n ∗ n ** (m−1). Prueba esta función en un algoritmo general.'''

def potencia_de_numero(b,e):
    if e == 0:
        return 1
    return b * potencia_de_numero(b, e - 1)

num_int = int(input("Ingrese un número base: "))
exponente = int(input("Ingrese el exponente: "))
print(f'{num_int} elevado a la {exponente} es: {potencia_de_numero(num_int, exponente)}')


'''4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.'''

def entero_a_binario(entero):
    if entero == 0:
        return "0"
    if entero == 1:
        return "1"
    return entero_a_binario(entero // 2) + str(entero % 2)

num_int = int(input("Ingrese un número a convertir a binario: "))
print(entero_a_binario(num_int))

'''5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().'''


def es_palindromo(palabra):
    if len(palabra) <= 1:
       return True

    if palabra[0] != palabra[-1]:
        return False    
    
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra sin espacios ni acentos: ")
print(f"La palabra es palindromo: {es_palindromo(palabra)}")

'''Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)'''

def suma_digitos(n):
    if n // 10 == 0:
        return n
    
    return suma_digitos(n // 10) + n % 10

num_int = int(input("Ingrese el número para sumar sus dígitos: "))
print(f'La suma de los digitos es: {suma_digitos(num_int)}')

'''Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)'''

def contar_bloques(n):
    if n == 1:
        return n
    
    return contar_bloques(n - 1) + n

num_int = int(input("Ingrese el número de bloques en la base: "))
print(f'La suma de los digitos es: {contar_bloques(num_int)}')

'''Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0'''

def contar_digito(numero, digito):
    if digito < 0 or digito > 9:
        return "Ingrese un dígito entre el 0 y el 9."
    
    if numero == 0:
        return 0
    
    if numero % 10 == digito:
         return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
num_int = int(input("Ingrese el número: "))
digito = int(input("Ingrese el digito: "))

print(f'La cantidad de veces que se repite el dígito en el numero es: {contar_digito(num_int, digito)}')