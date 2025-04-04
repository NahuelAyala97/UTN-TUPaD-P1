#Trabajo prácito Nº3 Estructuras condicionales

''' Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.'''

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

''' Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.'''

nota = float(input("Ingrese la nota obtenida: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

'''
Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
'''

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("Por favor, ingrese un número par.")

'''
Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.Escribir un programa que solicite 
'''

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a.")
elif 12 <= edad <= 18:
    print("Adolescente.")
elif 18 <= edad <= 30:
    print("Adulto/a joven.")
else:
    print("Adulto/a.")

'''
Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
'''

password = input("Ingrese una contraseña (8 a 14 caracteres): ")

numCaracteres = len(password)

if 8 <= numCaracteres <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

'''
El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números.
escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
'''

from statistics import mode, median, mean

import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Hay sesgo positivo.")
elif media < mediana < moda:
    print("Hay sesgo negativo.")
elif media == mediana == moda:
    print("Sin sesgo.")

'''
Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
'''

frase = input("Ingrese una frase: ").casefold()
vocales = ("a","e","i","o","u")

if frase.endswith((vocales)):
    print(frase.capitalize() + '!')
else:
    print(frase.capitalize())

'''
Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
'''

nombre = input("Ingrese su nombre: ")
opcion = int(input(f'''Opciones:
1: Si quiere su nombre en mayúsculas.
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra mayúscula.
Ingrese la opción elegida: '''))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Ingrese una opción correcta, por favor.")

'''
Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
'''

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve.")
elif 3 <= magnitud < 4:
    print("Muy leve.")
elif 4 <= magnitud < 5:
    print("Moderado.")
elif 5 <= magnitud < 6:
    print("Fuerte.")
elif 6 <= magnitud < 7:
    print("Muy fuerte.")
elif 7 <= magnitud:
    print("Extremo.")

'''
Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
'''

hemisferio = input("Ingrese su hemisferio (N = Norte ó S = Sur): ").upper()
mes = input("Ingrese el mes actual: ").lower()
dia = int(input("Ingrese el día: "))


if hemisferio == "N":
    print("estoy aqui")
    if (mes == "diciembre" and 21 <= dia) or (mes == "marzo" and dia <= 20):
        print("Invierno.")
    elif (mes == "marzo" and 21 <= dia) or (mes == "junio" and dia <= 20):
        print("Primavera.")
    elif (mes == "junio" and 21 <= dia) or (mes == "septiembre" and dia <= 20):
        print("Verano.")
    elif (mes == "septiembre" and 21 <= dia) or (mes == "diciembre" and dia <= 20):
        print("Otoño.")
elif hemisferio == "S":
    if (mes == "diciembre" and 21 <= dia) or (mes == "marzo" and dia <= 20):
        print("Verano.")
    elif (mes == "marzo" and 21 <= dia) or (mes == "junio" and dia <= 20):
        print("Otoño.")
    elif (mes == "junio" and 21 <= dia) or (mes == "septiembre" and dia <= 20):
        print("Invierno.")
    elif (mes == "septiembre" and 21 <= dia) or (mes == "diciembre" and dia <= 20):
        print("Primavera.")
else:
    print("Hemisferio no valido.")