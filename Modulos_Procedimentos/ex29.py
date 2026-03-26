# 29. Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

def calc(tipo, valor):
    if tipo == 1:
        return valor * 1.03
    elif tipo == 2:
        return valor * 1.05     

def verifica_tipo(tipo):
    if tipo < 1 or tipo > 2:
        return exit(0)

def main():
    print("Informe o tipo de investimento:")
    print("1 - Poupanca")
    print("2 - Renda fixa")
    tipo = int(input("Opcao: "))
    verifica_tipo(tipo)
    valor = float (input("Informe o valor do investimento: R$"))
    print(f"Renda apos 30 dias: R${calc(tipo, valor)}")


if __name__ == "__main__":
    main()