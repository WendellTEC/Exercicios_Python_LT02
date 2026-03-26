# 26. Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

# Globais
n1: int = 0
n2: int = 0
maior: int = 0
menor: int = 0

def ordenar_valores():
    global n1, n2, maior, menor
    if n1 >= n2:
        maior = n1 
        menor = n2
    else:
        maior = n2
        menor = n1
    
def verifica_multiplo():
    global maior, menor
    if maior % menor == 0:
        print("Multiplo!")
    else:
        print("Nao multiplo!")

def main():
    global n1, n2 
    n1 = int(input("Informe n1: "))
    n2 = int(input("Informe n2: "))
    ordenar_valores()
    verifica_multiplo()

if __name__ == "__main__":
    main()