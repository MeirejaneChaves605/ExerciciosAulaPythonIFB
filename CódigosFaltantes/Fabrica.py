'''''
1. O custo ao consumidor de um carro novo é a soma do custo
de fábrica com a porcentagem do distribuidor e dos impostos
(aplicados ao custo de fábrica). Supondo que a porcentagem
do distribuidor seja de 12% do preço de fábrica e os impostos
de 30% do preço de fábrica, fazer um programa em Python
para ler o custo de fábrica de um carro e imprimir o custo ao
consumidor.

'''''

# lê o custo de fábrica
custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))
# calcula a porcentagem do distribuidor e dos impostos (sobre o custo
de fábrica)
percent_distribuidor = 0.12 * custo_fabrica
impostos = 0.30 * custo_fabrica
# calcula o custo final ao consumidor
custo_final = custo_fabrica + percent_distribuidor + impostos
# exibe o resultado
print(f"Custo ao consumidor: R$ {custo_final:.2f}")
