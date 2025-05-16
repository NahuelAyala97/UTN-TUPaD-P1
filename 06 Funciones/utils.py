import math


#Ejercicio 1
def imprimir_hola_mundo():
    return print("Hola mundo")

#Ejercicio 2
def saludar_usuario(nombre):
    return print(f"Hola {nombre}")

#Ejercicio 3
def información_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4
def calcular_area_circulo(radio): 
    area = math.pi * radio ** 2
    return area 

def calcular_perimetro_circulo(radio): 
    perimetro = 2 * math.pi * radio
    return perimetro

#Ejercicio 5
def segundos_a_horas(segundos):
    horas = segundos / 60
    return horas

#Ejercicio 6
def tabla_multiplicar(numero): 
    contador = 1
    while contador < 11:
        resultado = numero * contador
        print(f"{numero} X {contador} = {resultado}")
        contador += 1

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b == 0:
        division = "No es posible diviri por cero."
    else:
        division = a // b
    
    return print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}")

#Ejercicio 8 
def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        return "Ingrese valores mayores a cero, por favor."
    
    imc = peso / (altura ** 2)

    return round(imc, 2)

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#Ejercicio 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio