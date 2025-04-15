def calculate() -> float:
    pass

op = input("escriba su operacion")

while True:
    if (op[2] == "+"):
        print("Resultado: " + str(sumar(int(op[0]), int(op[4]))))
        break;
    else if(op[2] == "-"):
        print("Resultado: " + str(restar(int(op[0]), int(op[4]))))
        break;
    else if(op[2] == "*"):
        print("Resultado: " + str(multiplicar(int(op[0]), int(op[4]))))
        break;
    else if(op[2] == "/" and op[4] != 0):
        print("Resultado: " + str(dividir(int(op[0]), int(op[4]))))
        break;
    else:
        print("Input no valido")


def restar(a, b):
    return a - b

def sumar(a, b):
    return a + b  
    
def dividir(a, b):
    return a / b

def multiplicar(a, b):
    return a * b
