# Trabajo práctico Nº4: Estructuras repetitivas. 

'''
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
'''

contador = 0 

while contador <= 100: 
    print(f'{contador}\n')
    contador += 1

'''
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
'''

numero = int(input("Ingrese un número entero: "))
digitos = 0

if numero == 0: 
    digitos = 1
    print(f"La cantidad de digitos es {digitos}")
else: 
    numero = abs(numero)
    while numero > 0:
        numero //= 10
        digitos += 1 

print(f'El número de dgitos es {digitos}')

'''
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
'''

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número mayor al anterior: "))
suma = 0 

for num in range(num1 + 1, num2):
    suma += num 

print(f"La suma de los números entre los dos enteros es {suma}.")

'''
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
'''

numero = int(input("Ingrese un número: \n Para salir aprete 0. \n"))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número: \n Para ver el total aprete 0. \n"))

print(f'La suma total de los números ingresados es {suma}')

'''
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
'''

import random

numero_aleatorio = random.randint(0,9)
intentos = 0

num_usuario = int(input("Ingrese un número a adivinar entre el 0 y 9: "))

while num_usuario != numero_aleatorio:
    intentos += 1
    num_usuario = int(input('No adivinaste el número, intente de nuevo: '))

print(f"Adivinaste el número {numero_aleatorio}, realizaste {intentos} intentos.")

'''
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
'''

for num in range(100, -1, -2):
    print(num)

'''
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
'''

num_usuario = int(input("Ingrese un número: "))
suma = 0

for num in range(0, num_usuario + 1):
    suma += num

print(f'La suma de los enteros entre el 0 y {num_usuario} es {suma}.')

'''
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
'''

par = 0
impar = 0
positivo = 0
negativo = 0

for i in range (1,101):
    num = int(input("Ingrese un número a clasificar: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1

print(f'La clasificación de los números ingresados es: \n pares: {par}\n impar: {impar} \n positivo: {positivo} \n negativo:{negativo}')

'''
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
'''

import statistics

numeros = []

for i in range (1,11):
    num = int(input("Agregue un número para realizar el calculo de la media: "))
    numeros.append(num)

media = statistics.mean(numeros)

print(f"La media de los números ingresados es: {media}.")

'''
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
'''

num = int(input('Ingrese un número: '))
num_saliente = 0

while num > 0:
    digito = num % 10
    num //= 10
    num_saliente = num_saliente * 10 + digito

print(f'Número invertido: {num_saliente}')