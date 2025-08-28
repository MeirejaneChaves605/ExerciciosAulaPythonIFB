'''''
Questão 11:

Escreva um programa em Python que simule o controle de uma sala de cinema. O cinema
possui 10 assentos numerados de 1 a 10, e o programa deve manter uma lista de ocupação
dos assentos (com valores booleanos, onde True indica ocupado e False indica livre). O usuário
poderá interagir com o sistema por meio de um menu com as seguintes opções: 1. Reservar
um assento 2. Liberar um assento 3. Mostrar mapa de ocupação (exibindo quais assentos
estão ocupados e quais estão livres) 4. Sair O programa deve impedir a reserva de assentos já
ocupados e a liberação de assentos que já estão livres. Utilizar função.

'''''

def inicializar_assentos(total_assentos=10):
"""
Inicializa a lista de assentos, onde False = Livre e True = Ocupado.
"""
return [False] * total_assentos # Cria uma lista com 10 assentos livres inicialmente

def mostrar_mapa_ocupacao(assentos):
"""
Exibe o mapa de ocupação dos assentos da sala.
'O' para ocupado, 'F' para livre.
"""
print("\n--- MAPA DE OCUPAÇÃO ---")
for i, ocupado in enumerate(assentos):
status = "O" if ocupado else "F"
print(f"Assento {i + 1:2d}: [{status}]")
print("-------------------------\n")

def reservar_assento(assentos):
"""
Tenta reservar um assento. Pede o número do assento e verifica a disponibilidade.
"""
mostrar_mapa_ocupacao(assentos)
while True:
try:
num_assento_str = input("Digite o número do assento que deseja reservar (1-10): ")
num_assento = int(num_assento_str)

if not (1 <= num_assento <= len(assentos)):
print("Número de assento inválido. Por favor, digite um número entre 1 e 10.")
elif assentos[num_assento - 1]: # Assentos são 0-indexed na lista
print(f"O Assento {num_assento} já está OCUPADO. Por favor, escolha outro.")
else:
assentos[num_assento - 1] = True # Marca como ocupado
print(f"Assento {num_assento} RESERVADO com sucesso!")
break # Sai do loop de reserva
except ValueError:
print("Entrada inválida. Por favor, digite um número inteiro para o assento.")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

def liberar_assento(assentos):
"""
Tenta liberar um assento. Pede o número do assento e verifica se está ocupado.
"""
mostrar_mapa_ocupacao(assentos)
while True:
try:
num_assento_str = input("Digite o número do assento que deseja liberar (1-10): ")

num_assento = int(num_assento_str)

if not (1 <= num_assento <= len(assentos)):
print("Número de assento inválido. Por favor, digite um número entre 1 e 10.")
elif not assentos[num_assento - 1]: # Assentos são 0-indexed na lista
print(f"O Assento {num_assento} já está LIVRE. Não é possível liberá-lo.")
else:
assentos[num_assento - 1] = False # Marca como livre
print(f"Assento {num_assento} LIBERADO com sucesso!")
break # Sai do loop de liberação
except ValueError:
print("Entrada inválida. Por favor, digite um número inteiro para o assento.")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

def exibir_menu():
"""
Exibe as opções do menu principal do sistema.
"""
print("\n--- MENU DE CONTROLE DE CINEMA ---")
print("1. Reservar um assento")
print("2. Liberar um assento")
print("3. Mostrar mapa de ocupação")
print("4. Sair")
print("----------------------------------")

def main():
"""
Função principal que gerencia o fluxo do programa de controle de cinema.
"""
assentos_sala = inicializar_assentos() # Inicializa todos os 10 assentos como livres

print("Bem-vindo ao Sistema de Controle de Cinema!")

while True:
exibir_menu()
opcao = input("Escolha uma opção: ").strip()

if opcao == '1':
reservar_assento(assentos_sala)
elif opcao == '2':
liberar_assento(assentos_sala)
elif opcao == '3':
mostrar_mapa_ocupacao(assentos_sala)
elif opcao == '4':
print("Saindo do Sistema de Controle de Cinema. Volte sempre!")
break # Encerra o loop e o programa
else:
print("Opção inválida. Por favor, escolha um número de 1 a 4.")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()