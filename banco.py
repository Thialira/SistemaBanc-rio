menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 800
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação deu falha! O valor informado é inválido, preencha um valor válido.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação deu falha! Você não tem saldo sufuciente.")

        elif excedeu_limite:
            print("Operação deu falha! Valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação deu falha! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação deu falha! O valor digitado é inválido.")

    elif opcao == "e":
        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:  R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")