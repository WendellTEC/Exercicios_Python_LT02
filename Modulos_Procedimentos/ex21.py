# 21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
# a. Se a média for >= 6,0 exibir “APROVADO”;
# b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
# c. Se a média for < 3,0 exibir “RETIDO”.

# Globais
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0
m : float = 0.0

def media():
    global n1, n2, n3, n4, m
    m = (n1 + n2 + n3 + n4) / 4
    print("Media: ", round(m, 2))

def mensagem():
    if m >= 6.0:
        print("APROVADO")
    elif m >= 3.0 and m < 6.0:
        print("EXAME")
    else:
        print("RETIDO")

def main():
    global n1, n2, n3, n4
    n1 = float(input("Informe n1: "))
    n2 = float(input("Informe n2: "))
    n3 = float(input("Informe n3: "))
    n4 = float(input("Informe n4: "))
    media()
    mensagem()

if __name__ == "__main__":
    main()