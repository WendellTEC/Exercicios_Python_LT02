# 20. Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

import math

# Globais
a: int = 0
b: int = 0
c: int = 0
delta: int = 0
x1: float = 0.0
x1: float = 0.0

def delta_proc():
    global a, b, c, delta
    delta = (b**2) - 4 * a * c

def get_raizes():
    global delta
    if delta > 0:
        x1_proc()
        x2_proc()
    elif delta == 0:
        x1_proc()
    else:
        print("Nao possui raizes reais!")

def x1_proc():
    global b, a, delta, x1
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("x1: ", round(x1, 2))
    
def x2_proc():
    global b, a, delta, x2
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("x2: ", round(x2, 2))

def main():
    global a, b, c
    a = int(input("Informe o valor de A: "))
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))
    delta_proc()
    get_raizes()

if __name__ == "__main__":
    main()