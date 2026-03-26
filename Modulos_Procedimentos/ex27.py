# 27. Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

def velocidade_media(voltas, metros, minutos):
    km = (voltas * metros) / 1000
    horas = minutos / 60
    return km / horas

def main():
    global n_voltas, metros, minutos
    voltas = int(input("Informe a quantidade de voltas: "))
    metros = int(input("Informe a extensao em metros: "))
    minutos = int(input("Informe a duracao em minutos: "))
    print(velocidade_media(voltas, metros, minutos), "Km/h")
    
    
if __name__ == "__main__":
    main()