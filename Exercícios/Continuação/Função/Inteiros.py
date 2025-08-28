'''''
Questão 2:

Faça um programa em Python que leia dois números inteiros quaisquer para as variáveis A e B,
efetue a troca dos valores de forma que A passe a armazenar o valor de B e que B passe
armazenar o valor de A e que imprima os valores trocados, usando função.

'''''

def trocar_valores(a, b):
"""
Troca os valores de duas variáveis.

Args:
a: O primeiro valor.
b: O segundo valor.

Returns:
tuple: Uma tupla contendo os valores trocados (b, a).
"""
# Em Python, a troca de valores pode ser feita de forma concisa:
return b, a

def main():
"""
Função principal que solicita dois números inteiros,
efetua a troca de seus valores e imprime o resultado.
"""
print("--- Troca de Valores entre Variáveis ---")

while True:
try:
# Solicita o primeiro número
num_a_str = input("Digite o valor para a variável A: ")
num_a = int(num_a_str)

# Solicita o segundo número
num_b_str = input("Digite o valor para a variável B: ")
num_b = int(num_b_str)

print(f"\nValores **antes** da troca: A = {num_a}, B = {num_b}")

# Chama a função para trocar os valores
# A função retorna uma tupla, que é desempacotada diretamente nas variáveis
a_trocado, b_trocado = trocar_valores(num_a, num_b)

print(f"Valores **depois** da troca: A = {a_trocado}, B = {b_trocado}")
break # Sai do loop se as entradas forem válidas

except ValueError:
print("Entrada inválida. Por favor, digite apenas números inteiros.\n")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}. Tente novamente.\n")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()