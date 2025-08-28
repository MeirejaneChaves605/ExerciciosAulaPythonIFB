'''''
Questão 7:

Faça um programa em Python que simula as operações de um banco. O programa deve
apresentar um menu com as seguintes opções: 1. Depositar (O programa deve pedir o valor a
ser depositado e somá-lo ao saldo) 2. Sacar (O programa deve pedir o valor a ser sacado e
subtrair do saldo, desde que o valor seja menor ou igual ao saldo disponível) 3. Consultar Saldo
(O programa deve exibir o saldo atual) 4. Sair (O programa termina) O programa deve manter
um saldo inicial de R$ 1000,00 e permitir ao usuário realizar depósitos e saques até que ele
escolha a opção "Sair", usando função.

'''''

def depositar(saldo):
"""
Solicita um valor para depósito e o adiciona ao saldo.

Args:
saldo (float): O saldo atual da conta.

Returns:
float: O novo saldo após o depósito.
"""
while True:
try:
valor_deposito_str = input("Digite o valor a ser depositado (R$): ")
valor_deposito = float(valor_deposito_str)

if valor_deposito <= 0:
print("O valor do depósito deve ser positivo. Tente novamente.")
else:
saldo += valor_deposito
print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
return saldo
except ValueError:
print("Valor inválido. Por favor, digite um número para o depósito.")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

def sacar(saldo):
"""
Solicita um valor para saque e o subtrai do saldo, se houver fundos.

Args:

saldo (float): O saldo atual da conta.

Returns:
float: O novo saldo após o saque, ou o saldo inalterado se o saque não for possível.
"""
while True:
try:
valor_saque_str = input("Digite o valor a ser sacado (R$): ")
valor_saque = float(valor_saque_str)

if valor_saque <= 0:
print("O valor do saque deve ser positivo. Tente novamente.")
elif valor_saque > saldo:
print(f"Saldo insuficiente! Seu saldo atual é de R$ {saldo:.2f}.")
else:
saldo -= valor_saque
print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
return saldo
except ValueError:
print("Valor inválido. Por favor, digite um número para o saque.")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

def consultar_saldo(saldo):
"""
Exibe o saldo atual da conta.

Args:
saldo (float): O saldo atual da conta.
"""
print(f"Seu saldo atual é de R$ {saldo:.2f}.")

def exibir_menu():
"""
Exibe as opções do menu principal do banco.
"""
print("\n--- MENU DO BANCO ---")
print("1. Depositar")
print("2. Sacar")
print("3. Consultar Saldo")
print("4. Sair")
print("---------------------")

def main():
"""
Função principal que gerencia o fluxo do programa,
interagindo com o usuário através do menu.
"""
saldo_conta = 1000.00 # Saldo inicial da conta

print("Bem-vindo ao Banco Python!")
print(f"Seu saldo inicial é de R$ {saldo_conta:.2f}.")

while True:
exibir_menu()
opcao_str = input("Escolha uma opção: ")

if opcao_str == '1':
saldo_conta = depositar(saldo_conta)
elif opcao_str == '2':
saldo_conta = sacar(saldo_conta)
elif opcao_str == '3':

consultar_saldo(saldo_conta)
elif opcao_str == '4':
print("Obrigado por usar o Banco Python. Volte sempre!")
break # Encerra o loop e o programa
else:
print("Opção inválida. Por favor, escolha um número de 1 a 4.")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()