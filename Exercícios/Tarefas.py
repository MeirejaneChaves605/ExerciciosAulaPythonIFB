'''''
10. Você foi contratado para desenvolver um pequeno sistema de
gerenciamento de uma lista de tarefas pessoais. Escreva um
programa em Python que utilize um menu interativo para
permitir ao usuário as seguintes opções:
 1. Adicionar uma nova tarefa
 2. Listar todas as tarefas
 3. Remover uma tarefa pelo nome
 4. Sair do programa
O programa deve manter as tarefas em uma lista e permitir
que o usuário realize várias operações até optar por sair.
Utilizar função.

'''''

# Lista que armazena as tarefas
tarefas = []
def adicionar_tarefa():
 tarefa = input("Digite a nova tarefa: ")
 if tarefa:
 tarefas.append(tarefa)
 print("Tarefa adicionada com sucesso!")
 else:
 print("Tarefa não pode ser vazia.")
def listar_tarefas():
 if tarefas:
 print("\nLista de Tarefas:")
 indice = 1
 for tarefa in tarefas:
 print(f"{indice}. {tarefa}")
 indice += 1
 else:
 print("Nenhuma tarefa cadastrada.")
def remover_tarefa():
 nome = input("Digite o nome exato da tarefa que deseja remover: ")
 if nome in tarefas:
 tarefas.remove(nome)
 print("Tarefa removida com sucesso!")
 else:
 print("Tarefa não encontrada.")
def menu():
 while True:
 print("\nMenu de Tarefas")
 print("1. Adicionar uma nova tarefa")
 print("2. Listar todas as tarefas")
 print("3. Remover uma tarefa pelo nome")
 print("4. Sair")

 opcao = input("Escolha uma opção (1-4): ")
 if opcao == '1':
 adicionar_tarefa()
 elif opcao == '2':
 listar_tarefas()
 elif opcao == '3':
 remover_tarefa()
 elif opcao == '4':
 print("Encerrando o programa. Até mais!")
 break
 else:
 print("Opção inválida. Tente novamente.")
# Executa o menu
menu()
