menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepositando...  R$ {valor:.2f}")
        else:
            print("Operação falhou. Valor informado é invalido!")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite_diario:
            print("Operação falhou! O valor de saque excede o limite diario.")
        elif excedeu_saque:
            print("Operação falhou! Número maximo de saques excedido.")
        elif valor > 0:
            limite += valor
            if limite > limite_diario:
                print("Operação falhou! O valor de saque excede o limite diario.")
                limite -= valor
            else:
                numero_saques += 1
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"\nSacando...  R$ {valor:.2f}")
        else:
            print("Operação falhou. Valor informado é invalido!")


    elif opcao == "e":
        print("\n================EXTRATO================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")
    elif opcao == "q":
        print("\nsaindo")
        break
    else:
        print("Operação invalida, selecione a opção correta")