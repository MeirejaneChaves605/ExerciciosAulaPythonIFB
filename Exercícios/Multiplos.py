'''''
9. Faça um programa em Python que imprima todos múltiplos de
x, entre 1 e 100, onde x é um número informado pelo usuário.
Utilizar função.

'''''
def imprimir_multiplos(x):
 print(f"Múltiplos de {x} entre 1 e 100:")
 for num in range(1, 101):
 if num % x == 0:
 print(num, end=' ')
 print() # para pular linha no final
# entrada do usuário
x = int(input("Digite um número inteiro: "))
imprimir_multiplos(x)