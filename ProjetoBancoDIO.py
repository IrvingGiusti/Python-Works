import textwrap

def menu():
    menu = """\n

========== Menu ==========
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova Conta
[lc]\tListar Conta
[nu]\tNovo Usuário
[q]\tSair
"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito R$ {valor:.2f}\n"
        print("\n=== Depóstio realizado com sucesso! ===")
    else:
        print("Valor Digitado está icorreto!")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = saldo < valor    
    excedeu_limite = valor > limite       
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saque:
        print("Você atigiu o limmite máximo de saques no dia!")

    elif excedeu_saldo:
        print("Você não possui saldo suficiente para essa operação!")

    elif excedeu_limite:
        print("Você excedeu o valor máximo para saques!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("A operação falhou. O valor informado é inválido!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n############## EXTRATO ##############")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nsaldo: R$ {saldo:.2f}")
    print("#######################################")

def cadastrar_usuario(usuarios):
    
    cpf = input("Informe o número do CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n----- CPF Já cadastrado! -----")
        return
    
    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data de nascimento": data_nascimento, "endereço": endereco })

    print("----- Cliente cadastrado com sucesso -----")

def filtrar_usuario(cpf, usuarios):
    clientes_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("\n----- Conta criada com sucesso -----")
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n----- Usuário não encontrado, encerrando criação de conta! -----")

def listar_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            extrato = exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)

             if conta:
                  contas.append(conta)

        elif opcao == "lc":
             listar_conta(contas)

        elif opcao == "q":
            print("""Obrigado por utilizar nossos serviços!
              Tenha um bom dia!""")
            break

        else:
            print("""A opção escolhida não é válida. 
Por favor escolha outra opção""")
            
main()