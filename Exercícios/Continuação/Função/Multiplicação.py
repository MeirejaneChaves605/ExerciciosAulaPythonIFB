'''''
Questão 8:

Faça um programa em Python que leia dois valores inteiros, x e y. Por meio de multiplicações
sucessivas, calcule e exiba a função de exponenciação xy (Obs: quando o valor de y for 0, não
importa o valor de x, o resultado sempre será 1. Utilizar função), usando função.

'''''

def calcular_potencia(base, expoente):
"""
Calcula a potência de um número (base elevado ao expoente)
usando multiplicações sucessivas.

Args:
base (int): O número base (x).
expoente (int): O expoente (y).

Returns:
float: O resultado da exponenciação (base^expoente).
Retorna 1 se o expoente for 0.
Lida com expoentes negativos.

"""
# Caso especial: qualquer número elevado a 0 é 1
if expoente == 0:
return 1

# Lidar com expoentes negativos
if expoente < 0:
# Calcula a potência com expoente positivo e inverte o resultado
# Ex: x^-y = 1 / x^y
resultado_positivo = 1
for _ in range(abs(expoente)): # Usa o valor absoluto do expoente para o loop
resultado_positivo *= base
return 1 / resultado_positivo

# Cálculo para expoentes positivos (multiplicações sucessivas)
resultado = 1
for _ in range(expoente):
resultado *= base
return resultado

def main():
"""
Função principal que solicita a base e o expoente ao usuário,
calcula a potência e exibe o resultado.
"""
print("--- Calculadora de Exponenciação (x^y) ---")
print("Calcularemos x elevado a y usando multiplicações sucessivas.")

while True:
try:
# Solicita a base (x)

x_str = input("\nDigite o valor da base (x - número inteiro): ")
x = int(x_str)

# Solicita o expoente (y)
y_str = input("Digite o valor do expoente (y - número inteiro): ")
y = int(y_str)

# Chama a função para calcular a potência
resultado = calcular_potencia(x, y)

# Exibe o resultado
print(f"\n{x} elevado a {y} é igual a: **{resultado}**\n")
break # Sai do loop se a entrada for válida e o cálculo for feito

except ValueError:
print("Entrada inválida. Por favor, digite apenas números inteiros para x e y.\n")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.\n")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()