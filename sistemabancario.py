menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        
        
        valor_deposito = float(input("Quanto deseja depositar ? \n"))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"

        else:
            print("Operação falhou!!! Valor inválido!!")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou!! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou!! Numéro máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque : R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou!! o vvalor informado é invalido.")
    
    elif opcao == "e":
        print("\n============= Extrato =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=====================================")

    
    elif opcao == "q":
        break

    else:
        print("Opção invalida, por favor selecione novamente a opção desejada.")