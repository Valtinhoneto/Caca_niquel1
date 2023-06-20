import random


MAX_LINHAS = 3
MIN_BET = 1
MAX_BET = 100
COLUNAS = 3
FILEIRAS = 3

simbolo_contagem = {

    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


simbolo_valor= {

    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def slot_machine(rows, cols, simbolos):
    all_simbolos = []
    for simbolo, simbolo_contagem in simbolos.items():
        for i in range(simbolo_contagem):
            all_simbolos.append(simbolo)


    colunas = []
    for _ in range(cols):
        coluna = []
        saldo_simbolos = all_simbolos[:]
        for _ in range(rows):
            valor = random.choice(saldo_simbolos)
            saldo_simbolos.remove(valor)
            coluna.append(valor)

        colunas.append(coluna)

    return colunas


def tela_slot_machine (colunas):
    for row in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas)-1 :
                print(coluna[row], end = " | ")
            else:
                print(coluna [row], end = " | ")
        print()


def deposito():
    while True:
        valor = input("Qual o valor do seu deposito? R$ ")
        if valor.isdigit():
            valor = int(valor)
            if valor > 0:
                break
            else:
                print("O valor precisa ser maior que zero")
        else:
            print("Digite um numero")
    return valor

def numero_de_linhas():
    while True:
        linhas = input("Digite o numero de linhas para apostar de (1-" + str(MAX_LINHAS) + ") ?")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print("Digite o valor valido de linhas")
        else:
            print("Digite um numero")
    return linhas


def pegar_aposta():
    while True:
        valor = input("Qual o valor do seu apostar? R$ ")
        if valor.isdigit():
            valor = int(valor)
            if MIN_BET <= valor <= MAX_BET :
                break
            else:
                print(f"O valor precisa estar em mínimo e o maximo de aposta ${MIN_BET} - ${MAX_BET}")
        else:
            print("Digite um numero")
    return valor

def check_vencer(colunas, linhas , bet , valor):
    placar  = 0
    placar_linas = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            simbolo_check = coluna[linha]
            if simbolo != simbolo_check:
                break
        else:
            placar += valor[simbolo] * bet
            placar_linas.append(linha +1)

    return placar, placar_linas


def spin(balanco):
    linhas = numero_de_linhas()


    while True:
        bet = pegar_aposta()
        total_bet = bet * linhas

        if total_bet > balanco:
            print(f"Vc não possui dinheiro suficiente para apostar esse valor, seu saldo é {balanco}")

        else:
            break

    print(f" vc está apostando ${balanco}, em {linhas} linhas, A aposta total é {total_bet} ")

    slot = slot_machine(COLUNAS, FILEIRAS, simbolo_contagem)
    tela_slot_machine(slot)

    placar, placar_linhas = check_vencer(slot, linhas, bet, simbolo_valor)

    print(f"Você venceu ${placar}")
    print(f"você ganhou", *placar_linhas)

    return placar - total_bet

def main():

    balanco = deposito()
    while True:
        print(f"Seu saldo é $ {balanco}")
        user_input = input(" aperte entrer para girar (q para sair)")
        if user_input == "q":
            break
        balanco += spin(balanco)

main()