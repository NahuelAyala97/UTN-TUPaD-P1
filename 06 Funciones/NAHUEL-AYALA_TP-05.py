import utils

def main():
    utils.imprimir_hola_mundo()
    utils.saludar_usuario("Nahuel")
    utils.información_personal("Nahuel", "Ayala", 28, "Argentina")

    radio = (float(input("Ingrese el radio de un circulo: ")))
    print(f"El area del circulo es {utils.calcular_area_circulo(radio)}")
    print(f"El perimetro del circulo es {utils.calcular_perimetro_circulo(radio)}")

    segundos = (int(input("Ingrese los segundos a convertir: ")))
    print(f"Los segundos son {utils.segundos_a_horas(segundos)} horas.")

    numero = (int(input("Ingrese un numero: ")))
    utils.tabla_multiplicar(numero)  

    num1 = int(input("Ingrese el primer número: "))  
    num2 = int(input("Ingrese el segundo número: "))  
    utils.operaciones_basicas(num1, num2)

    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))
    print(f"Si IMC es: {utils.calcular_imc(peso, altura)}")

    celsius = float(input("Ingrese los grados Celsius: "))
    print(f"{celsius}°C equivalen a {utils.celsius_a_fahrenheit(celsius)}°F")

    list_num = []
    for i in range(3):
       list_num.append( int(input("Ingrese un número: ")))
    print(f"El promedio entre los tres número es: {utils.calcular_promedio(list_num[0], list_num[1], list_num[2])}")


main()