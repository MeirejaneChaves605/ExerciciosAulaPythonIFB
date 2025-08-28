'''''
13. Uma universidade está organizando os dados de
participação dos alunos em dois eventos acadêmicos: uma
palestra sobre Inteligência Artificial e um workshop de
Programação em Python. Os dados de presença são
armazenados em dois conjuntos distintos: palestra_ia e
workshop_python, contendo os nomes dos alunos que
participaram de cada evento. Escreva um programa em
Python com o seguinte menu interativo:
 1. Adicionar aluno a um evento: O programa deve perguntar
o nome do aluno e em qual evento ele participou (IA ou
Python) e adicionar o nome ao conjunto correspondente.
 2. Mostrar alunos que participaram de ambos os eventos:
Exiba os nomes que aparecem nos dois conjuntos
(interseção).
 3. Mostrar alunos que participaram somente da palestra de
IA: Exiba os nomes que estão no conjunto da palestra, mas
não no workshop (diferença).
4. Mostrar alunos que participaram de pelo menos um evento:
Exiba a união dos dois conjuntos, sem repetições.
5. Verificar participação de um aluno: Solicite o nome de um
aluno e diga se ele participou de ambos, somente um ou
nenhum dos eventos.
6. Sair
O programa deve funcionar em laço até que o usuário
escolha a opção de sair. Utilize operações com conjuntos
(union, intersection, difference) para resolver as tarefas.
Utilizar função.

'''''

# Conjuntos para armazenar os nomes dos alunos
palestra_ia = set()
workshop_python = set()
def adicionar_aluno():
 nome = input("Nome do aluno: ").strip()
 evento = input("Evento (IA ou Python): ").strip().lower()
 if evento == "ia":
 palestra_ia.add(nome)
 print(f"{nome} adicionado à palestra de IA.")
 elif evento == "python":
 workshop_python.add(nome)
 print(f"{nome} adicionado ao workshop de Python.")
 else:
 print("Evento inválido. Digite apenas 'IA' ou 'Python'.")
def mostrar_ambos():
 ambos = palestra_ia.intersection(workshop_python)
 print("\nAlunos que participaram de ambos os eventos:")
 if ambos:
 for aluno in ambos:
 print(aluno)
 else:
 print("Nenhum aluno participou de ambos os eventos.")
def mostrar_so_ia():
 somente_ia = palestra_ia.difference(workshop_python)
 print("\nAlunos que participaram somente da palestra de IA:")
 if somente_ia:
 for aluno in somente_ia:
 print(aluno)
 else:
 print("Nenhum aluno participou somente da palestra de IA.")
def mostrar_pelo_menos_um():
 pelo_menos_um = palestra_ia.union(workshop_python)
 print("\nAlunos que participaram de pelo menos um evento:")
 if pelo_menos_um:
 for aluno in pelo_menos_um:
 print(aluno)
 else:
 print("Nenhum aluno participou de eventos.")
def verificar_participacao():
 nome = input("Digite o nome do aluno a verificar: ").strip()
 em_ia = nome in palestra_ia
 em_python = nome in workshop_python
 print()
 if em_ia and em_python:
 print(f"{nome} participou de ambos os eventos.")
 elif em_ia:
 print(f"{nome} participou somente da palestra de IA.")
 elif em_python:
 print(f"{nome} participou somente do workshop de Python.")
 else:
 print(f"{nome} não participou de nenhum evento.")
def menu():
 while True:
 print("\n--- MENU ---")
 print("1. Adicionar aluno a um evento")
 print("2. Mostrar alunos que participaram de ambos os eventos")
 print("3. Mostrar alunos que participaram somente da palestra de
IA")
 print("4. Mostrar alunos que participaram de pelo menos um
evento")
 print("5. Verificar participação de um aluno")
 print("6. Sair")
 opcao = input("Escolha uma opção: ").strip()
 if opcao == "1":
 adicionar_aluno()
 elif opcao == "2":
 mostrar_ambos()
 elif opcao == "3":
 mostrar_so_ia()
 elif opcao == "4":
 mostrar_pelo_menos_um()
 elif opcao == "5":
 verificar_participacao()
 elif opcao == "6":
 print("Encerrando o programa.")
 break
 else:
 print("Opção inválida. Tente novamente.")
def main():
 menu()
if __name__ == "__main__":
 main()