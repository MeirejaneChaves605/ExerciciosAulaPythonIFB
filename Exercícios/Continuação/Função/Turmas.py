'''''
Questão 12:

Uma escola aplicou provas em várias turmas e deseja registrar as maiores notas obtidas por
seus alunos. Cada nota é representada por uma tupla no formato: (nome_do_aluno, nota,
disciplina). Escreva um programa com o seguinte menu interativo: 1. Adicionar nota: o usuário
deve informar o nome do aluno, a nota (float) e a disciplina, e esses dados devem ser
adicionados como uma nova tupla à lista. 2. Mostrar melhor aluno por disciplina: para cada
disciplina presente na lista, exiba o nome do aluno com a maior nota. 3. Consultar notas por
aluno: o usuário digita o nome de um aluno e o programa mostra todas as notas dele, com a
respectiva disciplina. 4. Exibir notas ordenadas (decrescente): mostre todas as tuplas da lista
ordenadas da maior para a menor nota, no formato (nota, nome_do_aluno, disciplina). 5. Sair
O programa deve funcionar em laço até que o usuário escolha a opção de sair. Use tuplas para
armazenar as notas e manipule-as sem alterar sua estrutura original. Utilizar função.

'''''

def adicionar_nota(notas):
"""
Solicita nome do aluno, nota e disciplina, e adiciona como uma tupla à lista.
Realiza validação de entrada para nota (float entre 0 e 10).

"""
nome = input("\nDigite o nome do aluno: ").strip()
disciplina = input("Digite a disciplina: ").strip()

while True:
try:
nota_str = input("Digite a nota (0.0 a 10.0): ")
nota = float(nota_str)
if 0.0 <= nota <= 10.0:
break
else:
print("Nota inválida. A nota deve ser entre 0.0 e 10.0.")
except ValueError:
print("Entrada inválida. Por favor, digite um número para a nota.")

nova_nota = (nome, nota, disciplina)
notas.append(nova_nota)
print(f"Nota de '{nome}' em '{disciplina}' ({nota:.1f}) adicionada com sucesso!\n")

def mostrar_melhor_aluno_por_disciplina(notas):
"""
Para cada disciplina, exibe o nome do aluno com a maior nota.
"""
if not notas:
print("\nNenhuma nota cadastrada para analisar.")
return

melhores_por_disciplina = {} # Dicionário para armazenar a maior nota por disciplina

for nome, nota, disciplina in notas:
# Se a disciplina ainda não está no dicionário OU

# se a nota atual é maior que a nota já registrada para essa disciplina
if disciplina not in melhores_por_disciplina or nota >
melhores_por_disciplina[disciplina]["nota"]:
melhores_por_disciplina[disciplina] = {"nome": nome, "nota": nota}

print("\n--- Melhores Alunos por Disciplina ---")
if not melhores_por_disciplina:
print("Nenhum dado disponível para as disciplinas.")
else:
for disciplina, info in melhores_por_disciplina.items():
print(f"Disciplina: {disciplina} | Melhor Aluno: {info['nome']} | Nota: {info['nota']:.1f}")
print("--------------------------------------\n")

def consultar_notas_por_aluno(notas):
"""
Solicita o nome de um aluno e exibe todas as suas notas.
"""
if not notas:
print("\nNenhuma nota cadastrada para consultar.")
return

nome_busca = input("\nDigite o nome do aluno para consultar as notas: ").strip()

notas_encontradas = []
for nome, nota, disciplina in notas:
if nome.lower() == nome_busca.lower(): # Busca case-insensitive
notas_encontradas.append((disciplina, nota))

if notas_encontradas:
print(f"\n--- Notas de {nome_busca.capitalize()} ---")
for disciplina, nota in notas_encontradas:

print(f"Disciplina: {disciplina} | Nota: {nota:.1f}")
print("--------------------------\n")
else:
print(f"Nenhuma nota encontrada para o aluno '{nome_busca}'.\n")

def exibir_notas_ordenadas(notas):
"""
Exibe todas as notas da lista, ordenadas da maior para a menor.
O formato da saída é (nota, nome_do_aluno, disciplina).
"""
if not notas:
print("\nNenhuma nota cadastrada para ordenar.")
return

# Cria uma cópia da lista de notas para ordenar
# A ordenação é feita pelo segundo elemento da tupla (a nota), em ordem decrescente
notas_ordenadas = sorted(notas, key=lambda x: x[1], reverse=True)

print("\n--- Notas Ordenadas (Decrescente) ---")
for nome, nota, disciplina in notas_ordenadas:
print(f"Nota: {nota:.1f} | Aluno: {nome} | Disciplina: {disciplina}")
print("-------------------------------------\n")

def exibir_menu():
"""
Exibe as opções do menu principal do sistema.
"""
print("\n--- MENU DE GERENCIAMENTO DE NOTAS ---")
print("1. Adicionar nota")
print("2. Mostrar melhor aluno por disciplina")
print("3. Consultar notas por aluno")

print("4. Exibir notas ordenadas (decrescente)")
print("5. Sair")
print("--------------------------------------")

def main():
"""
Função principal que gerencia o fluxo do programa,
interagindo com o usuário através do menu.
"""
todas_as_notas = [] # Lista principal que armazena as tuplas (nome, nota, disciplina)

print("Bem-vindo ao Sistema de Gerenciamento de Notas da Escola!")

while True:
exibir_menu()
opcao = input("Escolha uma opção: ").strip()

if opcao == '1':
adicionar_nota(todas_as_notas)
elif opcao == '2':
mostrar_melhor_aluno_por_disciplina(todas_as_notas)
elif opcao == '3':
consultar_notas_por_aluno(todas_as_notas)
elif opcao == '4':
exibir_notas_ordenadas(todas_as_notas)
elif opcao == '5':
print("Saindo do programa de gerenciamento de notas. Até logo!")
break
else:
print("Opção inválida. Por favor, escolha um número de 1 a 5.")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()