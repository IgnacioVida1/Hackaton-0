def calculate() -> float:
    pass
    

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

a = float(input("Ingrese el dividendo: "))
b = float(input("Ingrese el divisor: "))

resultado = dividir(a, b)
print("Resultado:", resultado)
