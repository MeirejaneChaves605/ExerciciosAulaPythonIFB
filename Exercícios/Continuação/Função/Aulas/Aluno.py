'''''
Crie um programa que peça ao usuário o nome de um aluno e
as três notas que ele obteve em uma disciplina, junto com o
peso de cada uma dessas notas (ou seja, a importância de
cada nota na média final). O programa deve calcular a média
ponderada do aluno e exibir o resultado com uma mensagem
personalizada.

'''''

nome = input("Digite o nome do aluno:")
nota1 = float(input("Digite a nota 1:"))
peso1 = float(input("Digite o peso da nota1:"))
nota2 = float(input("Digite a nota 2:"))
peso2 = float(input("Digite o peso da nota2:"))
nota3 = float(input("Digite a nota 3:"))
peso3 = float(input("Digite o peso da nota3:"))
media = (nota1*peso1 +nota2*peso2 + nota3*peso3)/(peso1*peso2*peso3)
print(f"\n{nome}, sua média ponderada é {media:.2f}")