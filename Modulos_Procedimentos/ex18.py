# 18. Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

# Globais
v1: int = 0
v2: int = 0

def dif():
    global v1, v2
    if v1 > v2:
        print(v1 - v2)
    else:
        print(v2 - v1)

def main():
    global v1, v2
    v1 = int(input("Informe o valor 1: "))
    v2 = int(input("Informe o valor 2: "))
    dif() 

if __name__ == "__main__":
    main()