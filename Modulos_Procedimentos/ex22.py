# 22. Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

# Globais
v1: int = 0
v2: int = 0

def verifica_diferentes():
    global v1, v2
    if v1 == v2:
        print("Error: Valores iguais")
        exit(0)
    
def ordem_crescente():
    global v1, v2
    if v1 > v2:
        print(v2, v1)
    else:
        print(v1, v2)
    
def main():
    global v1, v2
    v1 = int(input("Informe v1: "))
    v2 = int(input("Informe v2: "))
    verifica_diferentes()
    ordem_crescente()

if __name__ == "__main__":
    main()