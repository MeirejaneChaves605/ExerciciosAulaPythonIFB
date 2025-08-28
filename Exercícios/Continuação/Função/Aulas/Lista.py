'''''
Exercício da apostila da aula Estrutura de dados e funções de python

Você vai criar um programa que gerencia uma lista de tarefas. O programa deve: 1. Permitir que
o usuário adicione tarefas. Cada tarefa deve ter: Descrição (string), Prioridade (inteiro de 1 a 5,
onde 1 é a prioridade mais alta) e Status (inicialmente “pendente”); 2. Armazenar cada tarefa
como um dicionário com as chaves "descrição", "prioridade" e "status"; 3. Manter todas as
tarefas numa lista; 4. Criar funções para: Adicionar tarefas, Mostrar todas as tarefas ordenadas
por prioridade (da maior para a menor) e Marcar uma tarefa como concluída (alterar o status
para “concluída”); 5. Criar uma função main() que permita ao usuário escolher opções num
menu para: Adicionar tarefa, Listar tarefas, Marcar tarefa como concluída e Sair do programa.

'''''

def adicionar_tarefa(tarefas):
descricao = input("\nDescrição da tarefa: ")

while True:
prioridade_str = input("Prioridade (1-5, 1 = mais alta): ")
if prioridade_str.isdigit():
prioridade = int(prioridade_str)
if 1 <= prioridade <= 5:
break
else:
print("Por favor, digite um número inteiro entre 1 e 5.")
else:
print("Entrada inválida. Por favor, digite um número.")

tarefa = {
"descricao": descricao,
"prioridade": prioridade,
"status": "pendente"
}

tarefas.append(tarefa)
print("\nTarefa adicionada!\n")

def pegar_prioridade(tarefa):
return tarefa["prioridade"]

def listar_tarefas(tarefas):
if len(tarefas) == 0:
print("\nNenhuma tarefa cadastrada.\n")
return

tarefas.sort(key=pegar_prioridade)

print("\nTAREFAS:")

for i, t in enumerate(tarefas):
print(f"{i+1}. {t['descricao']} [Prioridade: {t['prioridade']}] - Status: {t['status']}")
print()

def marcar_concluida(tarefas):
if len(tarefas) == 0:
print("\nNenhuma tarefa cadastrada.\n")
return

listar_tarefas(tarefas)

while True:
escolha_str = input("\nDigite o número da tarefa a ser marcada como concluída: ")
if escolha_str.isdigit():
escolha = int(escolha_str)
if 1 <= escolha <= len(tarefas):
indice = escolha - 1
tarefas[indice]["status"] = "concluída" # Corrected "concluida" to "concluída"
print("\nTarefa marcada como concluída!\n")
break
else:

print("Número de tarefa inválido. Tente novamente!")
else:
print("Entrada inválida. Por favor, digite um número.")

def main():
tarefas = []
while True:
print("--- MENU ---")
print("1. Adicionar tarefa")
print("2. Listar tarefas")
print("3. Marcar tarefa como concluída")
print("4. Sair")

escolha = input("\nEscolha uma opção: ")

if escolha == '1':
adicionar_tarefa(tarefas)
elif escolha == '2':
listar_tarefas(tarefas)
elif escolha == '3':
marcar_concluida(tarefas)
elif escolha == '4':
print("\nSaindo do programa. Até mais!\n") # Added newline for consistency
break
else:
print("\nOpção inválida. Tente novamente!\n")

if __name__ == "__main__":
main()