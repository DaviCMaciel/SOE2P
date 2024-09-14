from ctypes import CDLL, c_float

dll = CDLL("./soma.dll")


dll.somaFloat.restype = c_float
dll.somaFloat.argtypes = (c_float, c_float)

def add():
    print("Digite 1 para calcular o soatorio de 2 números float ou 0 para finalizar: ")
    auxA = int(input())

    if auxA == 0:
     return False;

    if auxA == 1:
     num1 = float(input("Digite o primeiro número: "));
     num2 = float(input("Digite o segundo número: "))
     soma = dll.somaFloat(num1, num2)
     print(f"O resultado da soma de {num1} com {num2} é: {soma}")
     return True
    
    else: return True

def main ():
    while True:
     if not add():
        break
     

     
if __name__ == "__main__":
    main()