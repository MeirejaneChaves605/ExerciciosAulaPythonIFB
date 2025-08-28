'''''
Questão 1:

O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a porcentagem do
distribuidor seja de 12% do preço de fábrica e os impostos de 30% do preço de fábrica, fazer
um programa em Python para ler o custo de fábrica de um carro e imprimir o custo ao
consumidor, usando função.

'''''

def calcular_custo_consumidor(custo_fabrica):
"""
Calcula o custo final de um carro ao consumidor.

Args:
custo_fabrica (float): O custo de fábrica do carro.

Returns:
float: O custo total do carro para o consumidor.
"""
if custo_fabrica < 0:
raise ValueError("O custo de fábrica não pode ser negativo.")

porcentagem_distribuidor = 0.12 # 12%
porcentagem_impostos = 0.30 # 30%

valor_distribuidor = custo_fabrica * porcentagem_distribuidor
valor_impostos = custo_fabrica * porcentagem_impostos

custo_total = custo_fabrica + valor_distribuidor + valor_impostos
return custo_total

def main():
"""

Função principal que interage com o usuário para obter o custo de fábrica
e exibir o custo ao consumidor.
"""
print("--- Calculadora de Custo de Carro ao Consumidor ---")
while True:
try:
custo_fabrica_str = input("Digite o custo de fábrica do carro (R$): ")
custo_fabrica = float(custo_fabrica_str)

custo_final = calcular_custo_consumidor(custo_fabrica)
print(f"\nO custo ao consumidor do carro é: R$ {custo_final:.2f}\n")
break # Sai do loop se a entrada for válida
except ValueError as e:
print(f"Erro: {e}. Por favor, digite um valor numérico válido para o custo de fábrica.")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
main()