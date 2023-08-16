# Declarando as variáveis

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Iniciando loop

while True:

    opcao = input(menu)

# Função Deposito

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor:.2f}\n"

        else:
            print("Valor Digitado está icorreto!")

# Função Sacar

    elif opcao == "s":
        valor = float(input("Digite o valor que deseja sacar: "))

# Declarando váriaveis de comparação
            
        excedeu_saldo = saldo < valor
        
        excedeu_valor = valor > limite
        
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saque:
            print("Você atigiu o limmite máximo de saques no dia!")

        elif excedeu_saldo:
            print("Você não possui saldo suficiente para essa operação!")

        elif excedeu_valor:
            print("Você excedeu o valor máximo para saques!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("A operação falhou. O valor informado é inválido!")
    
# Função extrato

    elif opcao == "e":
        print("\n############## EXTRATO ##############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("#######################################")

# Finalizando o loop

    elif opcao == "q":
        print("""Obrigado por utilizar nossos serviços!
              Tenha um bom dia!""")
        break
    
# Em caso nenhuma das opções seja selecionada

    else:
        print("""A opção escolhida não é válida. 
Por favor escolha outra opção""")