from datetime import date
import datetime

nome = input("Informe seu come completo: ")
cpf = input("Informe o número do seu CPF (no formato xxx.xxx.xxx-xx): ")
# Pedir ao usuário que informe sua data de nascimento
while True:
    dataDeNascimento = input("Por favor, informe sua data de nascimento (no formato AAAA-MM-DD): ")
    
    # Tente converter a entrada do usuário em um objeto datetime
    try:
        data_nascimento = datetime.datetime.strptime(dataDeNascimento, "%Y-%m-%d")
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Formato de data inválido. Certifique-se de usar o formato YYYY-MM-DD.")

def calcularIdade(anoDeNascimento):
    today = date.today()
    age = today.year - anoDeNascimento.year - ((today.month, today.day) < (anoDeNascimento.month, anoDeNascimento.day))
    return age

idade = calcularIdade(data_nascimento)
print("Seu nome é " + nome + " seu CPF é " + cpf + f" e você tem {idade} anos.")