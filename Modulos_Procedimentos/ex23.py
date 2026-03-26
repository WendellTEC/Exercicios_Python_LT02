# 23. Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

# Globais
v1: int = 0
v2: int = 0
v3: int = 0
v4: int = 0

def ordem_obrigatoria():
    global v1, v2, v3
    if v1 >= v2 or v1 >= v3:
        print("Error: Ordem incerta")
        exit(0)
    elif v2 >= v3: 
        print("Error: Ordem incerta")
        exit(0)
    
def ordem_crescente():
    global v1, v2, v3, v4
    if v4 <= v1:
        print(v4, v1, v2, v3)
    elif v4 >= v1 and v4 < v2:
        print(v1, v4, v2, v3)
    elif v4 >= v2 and v4 < v3:
        print(v1, v2, v4, v3)
    else:
        print(v1, v2, v3, v4)

def main():
    global v1, v2, v3, v4 
    v1 = int(input("Informe v1: "))
    v2 = int(input("Informe v2: "))
    v3 = int(input("Informe v3: "))
    v4 = int(input("Informe v4: "))
    ordem_obrigatoria()
    ordem_crescente()

if __name__ == "__main__":
    main()