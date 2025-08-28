'''''
Questão 10:

Você foi contratado para desenvolver um pequeno sistema de gerenciamento de uma lista de
tarefas pessoais. Escreva um programa em Python que utilize um menu interativo para
permitir ao usuário as seguintes opções: 1. Adicionar uma nova tarefa 2. Listar todas as tarefas
3. Remover uma tarefa pelo nome 4. Sair do programa O programa deve manter as tarefas em
uma lista e permitir que o usuário realize várias operações até optar por sair. Utilizar função.

'''''

def adicionar_tarefa(tarefas):
"""
Adiciona uma nova tarefa à lista.
Solicita a descrição da tarefa ao usuário.
"""
descricao = input("\nDigite a descrição da nova tarefa: ").strip()
if descricao:
tarefas.append(descricao)
print(f"Tarefa '{descricao}' adicionada com sucesso!")
else:
print("A descrição da tarefa não pode ser vazia.")

def listar_tarefas(tarefas):
"""
Lista todas as tarefas atualmente na lista.
"""
if not tarefas:
print("\nSua lista de tarefas está vazia.")

else:
print("\n--- SUAS TAREFAS ---")
for i, tarefa in enumerate(tarefas):
print(f"{i + 1}. {tarefa}")
print("--------------------")

def remover_tarefa(tarefas):
"""
Remove uma tarefa da lista pelo nome.
Solicita o nome da tarefa a ser removida.
"""
if not tarefas:
print("\nNão há tarefas para remover. Sua lista está vazia.")
return

listar_tarefas(tarefas) # Mostra a lista para o usuário escolher
tarefa_para_remover = input("\nDigite o nome (descrição exata) da tarefa que deseja
remover: ").strip()

if tarefa_para_remover in tarefas:
tarefas.remove(tarefa_para_remover)
print(f"Tarefa '{tarefa_para_remover}' removida com sucesso!")
else:
print(f"Tarefa '{tarefa_para_remover}' não encontrada na lista.")

def exibir_menu():
"""
Exibe o menu de opções para o usuário.
"""
print("\n--- MENU ---")
print("1. Adicionar nova tarefa")

print("2. Listar todas as tarefas")
print("3. Remover uma tarefa pelo nome")
print("4. Sair do programa")
print("------------")

def main():
"""
Função principal que gerencia o fluxo do programa,
interagindo com o usuário através do menu.
"""
tarefas = [] # Lista para armazenar as tarefas

print("Bem-vindo ao Gerenciador de Tarefas Pessoais!")

while True:
exibir_menu()
opcao = input("Escolha uma opção: ").strip()

if opcao == '1':
adicionar_tarefa(tarefas)
elif opcao == '2':
listar_tarefas(tarefas)
elif opcao == '3':
remover_tarefa(tarefas)
elif opcao == '4':
print("Saindo do programa. Suas tarefas foram salvas (nesta sessão). Até logo!")
break
else:
print("Opção inválida. Por favor, escolha um número de 1 a 4.")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente

if __name__ == "__main__":
main()