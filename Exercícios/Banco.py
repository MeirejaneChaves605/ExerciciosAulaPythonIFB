'''''
7. Faça um programa em Python que simula as operações de
um banco. O programa deve apresentar um menu com as
seguintes opções:
1. Depositar (O programa deve pedir o valor a ser depositado
e somá-lo ao saldo)
2. Sacar (O programa deve pedir o valor a ser sacado e
subtrair do saldo, desde que o valor seja menor ou igual ao
saldo disponível)
3. Consultar Saldo (O programa deve exibir o saldo atual)
4. Sair (O programa termina)
O programa deve manter um saldo inicial de R$ 1000,00 e
permitir ao usuário realizar depósitos e saques até que ele
escolha a opção "Sair".


'''''

saldo = 1000.00
while True:
 print("\nMenu:")
 print("1. Depositar")
 print("2. Sacar")
 print("3. Consultar Saldo")
 print("4. Sair")
 opcao = input("Escolha uma opção (1-4): ")
 if opcao == '1':
 valor = float(input("Digite o valor a depositar: R$ "))
 if valor > 0:
 saldo += valor
 print(f"Depósito realizado. Novo saldo: R$ {saldo:.2f}")
 else:
 print("Valor inválido. O depósito deve ser maior que zero.")
 elif opcao == '2':
 valor = float(input("Digite o valor a sacar: R$ "))
 if valor <= saldo and valor > 0:
 saldo -= valor
 print(f"Saque realizado. Novo saldo: R$ {saldo:.2f}")
 elif valor <= 0:
 print("Valor inválido. O saque deve ser maior que zero.")
 else:
 print("Saldo insuficiente para saque.")
 elif opcao == '3':
 print(f"Saldo atual: R$ {saldo:.2f}")
 elif opcao == '4':
 print("Encerrando o programa. Obrigado!")
 break
 else:
 print("Opção inválida. Digite um número entre 1 e 4.")