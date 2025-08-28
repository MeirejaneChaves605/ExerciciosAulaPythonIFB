
'''''
Questão 9:

Faça um programa em Python que imprima todos múltiplos de x, entre 1 e 100, onde x é um
número informado pelo usuário. Utilizar função.

'''''

def imprimir_multiplos(numero):
"""
Imprime todos os múltiplos de um dado 'numero' no intervalo de 1 a 100.

Args:
numero (int): O número do qual se deseja encontrar os múltiplos.
"""
if not isinstance(numero, int):
raise TypeError("O número deve ser um inteiro.")
if numero <= 0:
raise ValueError("O número deve ser um inteiro positivo.")

print(f"\n--- Múltiplos de {numero} entre 1 e 100 ---")

multiplos_encontrados = []
for i in range(1, 101): # Loop de 1 a 100 (inclusive)
if i % numero == 0: # Verifica se 'i' é um múltiplo de 'numero'
multiplos_encontrados.append(i)

if multiplos_encontrados:
print(", ".join(map(str, multiplos_encontrados)))

else:
print(f"Não foram encontrados múltiplos de {numero} entre 1 e 100.")
print("-------------------------------------------\n")

def main():
"""
Função principal que solicita um número ao usuário e chama
a função para imprimir seus múltiplos.
"""
print("--- Encontre os Múltiplos! ---")
print("Este programa irá listar todos os múltiplos de um número entre 1 e 100.")

while True:
try:
x_str = input("\nDigite um número inteiro positivo para encontrar seus múltiplos: ")
x = int(x_str)

imprimir_multiplos(x)
break # Sai do loop se a entrada for válida e a função for executada

except ValueError as e:
print(f"Erro na entrada: {e}. Por favor, digite um número inteiro positivo.")
except TypeError as e: # Captura o erro levantado pela função imprimir_multiplos
print(f"Erro: {e}")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()