'''''
Estrutura de controle e python
Crie um programa que simule o funcionamento de um caixa eletrônico. O usuário inicia com um
saldo fictício e pode realizar as seguintes operações através de um menu iterativo: 1.Consultar
saldo 2.Depositar dinheiro 3.Sacar dinheiro 4.Sair ● O programa deve repetir o menu até o
usuário escolher a opção 4 (sair).

'''''

saldo = 0.00

print("\n=== Bem-Vindo ao Caixa Eletrônico ===\n")

while True:
print("\n[ MENU ]")
print("1 - Consultar Saldo")
print("2 - Depositar Dinheiro")
print("3 - Sacar Dinheiro")
print("4 - Sair")

opcao = input("Escolha uma opção:")

if opcao == "1":
print(f"Saldo Atual: R$ {saldo:.2f}")
elif opcao == "2":
valor = float(input("Valor a depositar:"))
if valor > 0:
saldo = saldo + valor
print("Depósito realizado com sucesso!")
else:
print("valor inválido. Digite um valor positivo.")
elif opcao == "3":
valor = float(input("valor a sacar:"))
if valor <= 0:
print("valor inválido. Digite um valor positivo")
elif valor > saldo:
print("saldo insulficiente para o saque.")
else:
saldo -= valor
print("saque realizado com sucesso!")
elif opcao == "4":
print("obrigado por usar nosso sistema. Até logo!")
break
else:
print("opção Inválida! tente Novamente!")