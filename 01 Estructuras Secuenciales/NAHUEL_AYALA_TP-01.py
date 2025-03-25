#Trabajo práctico: Estructuras secuenciales. 
#Alumno: Nahuel Ayala


# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo")


'''
 Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla
'''

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


'''
Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
'''

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su país de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

'''
Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
'''
import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es {area} y el perimetro es {perimetro}.")

'''
Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
'''

segundos = int(input("Ingrese los segundos: "))
print(f"Los segundos ingresados son {segundos / 360} horas.")

'''
Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
'''

numero = int(input("Ingrese un número:"))
multiplicador = 1

while multiplicador <= 10:
    print(numero * multiplicador)
    multiplicador += 1


'''
Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
'''

num1 = int(input("Ingrese un número entero distino a 0:"))
num2 = int(input("Ingrese un número entero distino a 0:"))

print(f'''Suma: {num1 + num2}
Resta: {num1-num2}
Multiplicación: {num1 * num2}
División: {num1 / num2}''')    

'''
Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. 
'''

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kilos: "))

print(f"Si IMC es: {peso / altura ** 2}")


'''
Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit
'''

celsius = float(input("Ingrese la temperatura en Celsius: "))
farenheit = 9/5 * celsius + 32

print(f"La equivalencia en Farenheit es: {farenheit}")

'''
Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

print(f'El promedio de los tres números es: {(num1 + num2 + num3) / 3}')