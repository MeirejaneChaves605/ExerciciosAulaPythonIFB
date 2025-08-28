'''''
8. Faça um programa em Python que leia dois valores inteiros, x
e y. Por meio de multiplicações sucessivas, calcule e exiba a
função de exponenciação xy
 (Obs: quando o valor de y for 0,
não importa o valor de x, o resultado sempre será 1. Utilizar
função).

'''''

def main():
x = int(input("\nDigite o valor de x (base): "))
y = int(input("\nDigite o valor de y (expoente): "))

resultado = potencia(x, y)

print(f"\n{x} elevado a {y} = {resultado}")

def potencia(base, expoente):
if expoente == 0:
return 1

if expoente < 0:
return 1 / potencia(base, -expoente)

resultado = 1
for _ in range(abs(expoente)):
resultado *= base

return resultado

main()