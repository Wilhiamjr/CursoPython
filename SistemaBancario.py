opcoes = """

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(opcoes)
    opcao = float(input("Opção: "))

    if opcao == 1:
        valor = float(input("Valor: "))
        if not valor < 0:
            saldo += valor
            print('Você depositou ', valor, 'Seu novo saldo e de: ', saldo)
        else:
            print("Operação inválida informe um valor ")
    elif opcao == 2:
        valor = float(input("Valor: "))
        if valor > 0 and valor <= saldo and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            numero_saques += 1
            print('Você sacou ', valor, 'Seu novo saldo e de: ', saldo)
        elif valor > saldo and valor <= saldo+limite and numero_saques < LIMITE_SAQUES:
            print("Seu limite e de: ", saldo+limite, 'deseja sacar ?')
            opcao = int(input("1 - Sim, 2 - Não "))
            if opcao == 1:
                saldo += limite
                saldo -= valor
                numero_saques += 1
                print('Você sacou ', valor, 'Seu novo saldo e de: ', saldo)
        elif valor > saldo+limite and numero_saques < LIMITE_SAQUES:
            print("Seu limite e de: ", saldo+limite, 'Tente novamente')
        elif numero_saques >= LIMITE_SAQUES:
            print("Seu limite de saques e de: ", LIMITE_SAQUES, 'Você já exedeu o limite')
    elif opcao == 3:
        print("Seu EXTRATO e de saldo: ", saldo, 'Limite: ', limite, 'total de saques: ', numero_saques, 'LIMITE DE SAQUES: ', LIMITE_SAQUES, 'Total Saldo + Limite: ', saldo+limite)
    elif opcao == 4:
        break
    else:
        print("Opção inválida")