# 24. Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

# Globais
v: int = 0

def div_2():
    global v
    if v % 2 == 0:
        print("Divisivel por dois!")
    else:
        print("Nao divisivel por dois!")

def div_3():
    global v
    if v % 3 == 0:
        print("Divisivel por tres!")
    else:
        print("Nao divisivel por tres!")

def main():
    global v
    v = int(input("Informe o valor: "))
    div_2()
    div_3()

if __name__ == "__main__":
    main()