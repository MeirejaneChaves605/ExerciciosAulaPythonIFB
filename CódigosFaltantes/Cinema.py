'''''
11. Escreva um programa em Python que simule o controle de
uma sala de cinema. O cinema possui 10 assentos
numerados de 1 a 10, e o programa deve manter uma lista de
ocupação dos assentos (com valores booleanos, onde True
indica ocupado e False indica livre). O usuário poderá
interagir com o sistema por meio de um menu com as
seguintes opções:
 1. Reservar um assento
 2. Liberar um assento
 3. Mostrar mapa de ocupação (exibindo quais assentos
estão ocupados e quais estão livres)
 4. Sair

 '''''

11.
# Lista de ocupação: False = livre, True = ocupado
assentos = [False] * 10
def reservar_assento():
 numero = int(input("Digite o número do assento para reservar (1 a
10): "))
 if 1 <= numero <= 10:
 if assentos[numero - 1] == False:
 assentos[numero - 1] = True
 print(f"Assento {numero} reservado com sucesso.")
 else:
 print(f"O assento {numero} já está ocupado.")
 else:
 print("Número de assento inválido.")
def liberar_assento():
 numero = int(input("Digite o número do assento para liberar (1 a
10): "))
 if 1 <= numero <= 10:
 if assentos[numero - 1] == True:
 assentos[numero - 1] = False
 print(f"Assento {numero} liberado com sucesso.")
 else:
 print(f"O assento {numero} já está livre.")
 else:
 print("Número de assento inválido.")
def mostrar_mapa():
 print("\nMapa de Ocupação dos Assentos:")
 for i in range(10):
 if assentos[i] == True:
 status = "Ocupado"
 else:
 status = "Livre"
 print(f"Assento {i+1}: {status}")
 print()
def menu():
 while True:
 print("\n--- Menu do Cinema ---")
 print("1. Reservar um assento")
 print("2. Liberar um assento")
 print("3. Mostrar mapa de ocupação")
 print("4. Sair")
 opcao = input("Escolha uma opção (1-4): ")
 if opcao == '1':
 reservar_assento()
 elif opcao == '2':
 liberar_assento()
 elif opcao == '3':
 mostrar_mapa()
 elif opcao == '4':
 print("Encerrando o programa. Até logo!")
 break
 else:
 print("Opção inválida. Tente novamente.")
def main():
 menu()
# Ponto de entrada
if __name__ == "__main__":
 main()
