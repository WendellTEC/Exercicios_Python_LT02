# 25. Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

# Globais 
hi: int = 0
hf: int = 0
mi: int = 0
mf: int = 0
inicio: int = 0
fim: int = 0
duracao: int = 0

def converter_para_minutos():
    global hi, hf, mi, mf, inicio, fim
    inicio = hi * 60 + mi
    fim = hf * 60 + mf

def verifica_dia_seguinte():
    global fim, inicio
    if fim < inicio:
        fim += 24 * 60

def duracao_proc():
    global duracao, fim, inicio
    duracao = fim - inicio

def main():
    global hi, mi, hf, mf, duracao
    hi = int(input("Informe a hora de inicio: "))
    mi = int(input("Informe os minutos de inicio: "))
    hf = int(input("Informe a hora do fim: "))
    mf = int(input("Informe os minutos do fim: "))
    converter_para_minutos()
    verifica_dia_seguinte()
    duracao_proc()
    print(f"Duracao: {duracao // 60}h {duracao % 60}min")

if __name__ == "__main__":
    main()