'''''
2. Faça um programa em Python que leia dois números inteiros
quaisquer para as variáveis A e B, efetue a troca dos valores
de forma que A passe a armazenar o valor de B e que B
passe armazenar o valor de A e que imprima os valores
trocados.

'''''

# lê os valores de A e B
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
# faz a troca dos valores
temp = A
A = B
B = temp
# imprime os valores trocados
print(f"Depois da troca: A = {A}, B = {B}")