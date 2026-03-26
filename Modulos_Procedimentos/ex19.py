# 19. Receba 2 valores reais. Calcule e mostre o maior deles.

# Globais
v1: float = 0.0
v2: float = 0.0

def maior():
    global v1, v2
    if v1 > v2:
        print(v1)
    elif v1 < v2:
        print(v2)
    else:
        print("Valores iguais!")
    
def main():
    global v1,v2
    v1 = float(input("Informe o valor de v1: "))
    v2 = float(input("Informe o valor de v2: "))
    maior()

if __name__ == "__main__":
    main()