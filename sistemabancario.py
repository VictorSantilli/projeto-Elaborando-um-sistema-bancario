def menu():
    menu = """\n
    ============ Menu ==========
    [d]\tDpositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(menu)

def depositar ( saldo, valor_deposito, extrato, /): 
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito realizado com sucesso!!")
        else:
            print("Operação falhou!!! Valor inválido!!")
        return saldo, extrato

def sacar(*, saldo,valor,extrato,limite,numero_saques,limite_saques):

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > limite_saques

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

        return saldo, extrato

def mostrar_extrato(saldo, /,*, extrato):    
        print("\n============= Extrato =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=====================================")
 

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
          print("\n Já existe usuario com este CPF")
          return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço: ")

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})
    print("=== Usuario Criado com sucesso ===")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("=== Conta criada com sucesso ===")
        return {"Agencia": agencia, "numero_conta":numero_conta , "usuario":usuario}
    
    print("\nUsuario não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
     for conta in contas:
            linha = f"""\n
                    Agencia:\t{conta['agencia']}
                    C/C:\t{conta['numero_conta']}
                    Titular:\t{conta['usuario']['nome']}
                """
            print("=" * 100)
            print(linha)
           
def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            
            valor_deposito = float(input("Quanto deseja depositar ? \n"))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque:"))

            saldo , extrato  = sacar (saldo = saldo,
                                                valor = valor,
                                                extrato = extrato,
                                                limite = limite,
                                                numero_saques = numero_saques,
                                                LIMITE_SAQUES = LIMITE_SAQUES)

        
        elif opcao == "e":
            mostrar_extrato(saldo,extrato = extrato)
        
        elif opcao == "nu":
             criar_usuario(usuarios)

        elif opcao == "nc":
             
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA ,numero_conta,usuarios)

             if conta:
                  contas.append(conta)

        elif opcao == "lc":
             listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção invalida, por favor selecione novamente a opção desejada.")

main()