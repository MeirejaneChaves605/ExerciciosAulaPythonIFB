'''''
9. Faça um programa em Python que imprima todos múltiplos de
x, entre 1 e 100, onde x é um número informado pelo usuário.
Utilizar função.

'''''

def imprimir_multiplos(x):
print(f"\nMúltiplos de {x} entre 1 e 100")
for num in range(1,100):
if num % x == 0:
print(num, end= " ")
print()

def main():

x = int(input("\nDigite um número inteiro:"))
imprimir_multiplos(x)
main()