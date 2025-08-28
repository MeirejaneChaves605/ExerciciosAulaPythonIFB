'''''
8. Faça um programa em Python que leia dois valores inteiros, x
e y. Por meio de multiplicações sucessivas, calcule e exiba a
função de exponenciação xy
 (Obs: quando o valor de y for 0,
não importa o valor de x, o resultado sempre será 1. Utilizar
função).

'''''

def potencia(base, expoente):
 if expoente == 0:
 return 1
 resultado = 1
 for _ in range(expoente):
 resultado *= base
 return resultado
# leitura dos valores
x = int(input("Digite o valor de x (base): "))
y = int(input("Digite o valor de y (expoente): "))
# cálculo da potência
resultado = potencia(x, y)
# exibe o resultado
print(f"{x}^{y} = {resultado}")