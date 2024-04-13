menu = """
----- Sistema Bancário -----
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
____________________________

Selecione sua opção: """

saldo = 0
extrato = ""
limite_por_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Insira o valor do depósito: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"\nDepósito de R$ {deposito:.2f}"
        else:
            print("A operação falhou! O valor inserido é inválido.")

    elif opcao == "2":
        saque = (float(input("Insira o valor do saque: ")))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite_por_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("A operação falhou! Você excedeu o limite de saques por vez R$ 500.00")
        elif excedeu_saques:
            print("A operação falhou! Você excedeu o número de saques diários '3'. ")
        elif saque > 0:
            saldo -= saque
            extrato = f"Saque de R$ {saque:.2f}"
            numero_saques += 1
        else:
            print("A operação falhou! O valor inserido é inválido.")

    elif opcao == "3":
        print("****************************")
        print("          EXTRATO           ")
        print("Não houve movimentação!" if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("****************************")
    
    elif opcao == "4":
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida! Selecione uma opção válida.")