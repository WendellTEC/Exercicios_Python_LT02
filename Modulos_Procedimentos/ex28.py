# 28. Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
# Venda_Mensal	    Preço_Atual	    Preço_Novo
# < 500	            < 30	        + 10%
# >= 500 e < 1000	>= 30 e < 80	+15%
# >= 1000	        >= 80	        - 5%
# Obs.: para outras condições, preço novo será igual ao preço atual.

def novo_preco(preco_atual, media_mensal):
    if media_mensal < 500 and preco_atual < 30.0:
        return preco_atual * 1.1
    elif media_mensal >= 500 and media_mensal < 1000 and preco_atual >= 30.0 and preco_atual < 80.0:
        return preco_atual * 1.15
    elif media_mensal >= 1000 and preco_atual >= 80.0:
        return preco_atual * 0.95
    else: 
        return preco_atual

def main():
    preco_atual = float(input("Informe o preco atual: R$"))
    media_mensal = int(input("Informe a media de vendas mensal: "))
    print("Novo preco: ", novo_preco(preco_atual, media_mensal))

if __name__ == "__main__":
    main()