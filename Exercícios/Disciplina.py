'''''
12. Uma escola aplicou provas em várias turmas e deseja
registrar as maiores notas obtidas por seus alunos. Cada
nota é representada por uma tupla no formato:
(nome_do_aluno, nota, disciplina). Escreva um programa
com o seguinte menu interativo:
 1. Adicionar nota: o usuário deve informar o nome do aluno,
a nota (float) e a disciplina, e esses dados devem ser
adicionados como uma nova tupla à lista.
 2. Mostrar melhor aluno por disciplina: para cada disciplina
presente na lista, exiba o nome do aluno com a maior nota.
 3. Consultar notas por aluno: o usuário digita o nome de um
aluno e o programa mostra todas as notas dele, com a
respectiva disciplina.
4. Exibir notas ordenadas (decrescente): mostre todas as
tuplas da lista ordenadas da maior para a menor nota, no
formato (nota, nome_do_aluno, disciplina).
5. Sair
O programa deve funcionar em laço até que o usuário
escolha a opção de sair. Use tuplas para armazenar as notas
e manipule-as sem alterar sua estrutura original. Utilizar
função.

'''''

# Lista de tuplas no formato (nome, nota, disciplina)
notas = []
def adicionar_nota():
 nome = input("Nome do aluno: ")
 nota = float(input("Nota do aluno: ")) # sem verificação
 disciplina = input("Disciplina: ")
 notas.append((nome, nota, disciplina))
 print("Nota adicionada com sucesso.")
def melhor_por_disciplina():
 if len(notas) == 0:
 print("Nenhuma nota cadastrada.")
 return
 disciplinas = []
 for n in notas:
 if n[2] not in disciplinas:
 disciplinas.append(n[2])
 print("\nMelhor aluno por disciplina:")
 for d in disciplinas:
 melhor_nota = -1
 melhor_aluno = ""
 for n in notas:
 if n[2] == d and n[1] > melhor_nota:
 melhor_nota = n[1]
 melhor_aluno = n[0]
 print(f"{d}: {melhor_aluno} ({melhor_nota})")
def consultar_por_aluno():
 nome_busca = input("Digite o nome do aluno: ")
 encontrou = False
 for n in notas:
 if n[0].lower() == nome_busca.lower():
 print(f"{n[2]}: {n[1]}")
 encontrou = True
 if not encontrou:
 print("Nenhuma nota encontrada para este aluno.")
# Função auxiliar para usar como chave no sorted()
def obter_nota(tupla):
 return tupla[1]
def exibir_ordenadas():
 if len(notas) == 0:
 print("Nenhuma nota cadastrada.")
 return
 ordenadas = sorted(notas, key=obter_nota, reverse=True)
 print("\nNotas ordenadas (decrescente):")
 for n in ordenadas:
 print(f"{n[1]:.2f}, {n[0]}, {n[2]}")
def menu():
 while True:
 print("\n--- MENU DE NOTAS ---")
 print("1. Adicionar nota")
 print("2. Mostrar melhor aluno por disciplina")
 print("3. Consultar notas por aluno")
 print("4. Exibir notas ordenadas (decrescente)")
 print("5. Sair")
 opcao = input("Escolha uma opção (1-5): ")
 if opcao == '1':
 adicionar_nota()
 elif opcao == '2':
 melhor_por_disciplina()
 elif opcao == '3':
 consultar_por_aluno()
 elif opcao == '4':
 exibir_ordenadas()
 elif opcao == '5':
 print("Encerrando o programa.")
 break
 else:
 print("Opção inválida. Tente novamente.")
def main():
 menu()
if __name__ == "__main__":
 main()
