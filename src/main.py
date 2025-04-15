def calculate() -> float:
    pass



def restar(a, b):
    return a - b


a = int(input("Pon el primer numero "))
b = int(input("Pon el segundo numero "))
print(restar(a, b))

def sumar(a, b):
    return a + b  
  
def calculadora():
    print("Calculadora de Multiplicación (solo '*')")
    print("Escribe una operación (ejemplo: 5 * 3) y presiona Enter.")
    print("Presiona 'c' para borrar la operación o 'q' para salir.")

    while True:
        entrada = input(">> ")

        if entrada.lower() == 'q':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        elif entrada.lower() == 'c':
            print("Operación borrada.")
            continue
        elif '*' in entrada:
            try:
                operandos = entrada.split('*')
                if len(operandos) != 2:
                    print("Formato incorrecto. Usa el formato: número * número")
                    continue

                num1 = float(operandos[0].strip())
                num2 = float(operandos[1].strip())
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Error: asegúrate de ingresar números válidos.")
        else:
            print("Solo se permite la operación de multiplicación usando '*'. Usa 'c' para borrar o 'q' para salir.")

calculadora()

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

a = float(input("Ingrese el dividendo: "))
b = float(input("Ingrese el divisor: "))

resultado = dividir(a, b)
print("Resultado:", resultado)