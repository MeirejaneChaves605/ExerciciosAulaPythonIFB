'''''
Crie um programa em Python que recebe um valor em reais e o converte para outra moeda.
Use um menu para escolher a moeda de destino: 1. Dólar 2. Euro 3. Libra 4. Iene O programa
deve perguntar o valor em reais e exibir o valor convertido para a moeda escolhida. Use
valores fictícios para as taxas de conversão: 1 Real = 0.19 Dólar 1 Real = 0.17 Euro 1 Real = 0.15
Libra 1 Real = 25 Ienes, usando função.

'''''

def obter_taxas_conversao():
"""
Retorna um dicionário com as taxas de conversão fictícias de 1 Real para outras moedas.
"""
return {
"1": {"nome": "Dólar", "taxa": 0.19},
"2": {"nome": "Euro", "taxa": 0.17},
"3": {"nome": "Libra", "taxa": 0.15},
"4": {"nome": "Iene", "taxa": 25.0} # Iene é um valor inteiro grande, por isso float
}

def exibir_menu_moedas(taxas):
"""
Exibe o menu de opções de moedas para o usuário.
"""
print("\nEscolha a moeda de destino:")
for key, moeda_info in taxas.items():
print(f"{key}. {moeda_info['nome']}")

def converter_moeda(valor_reais, taxa_destino):
"""
Converte um valor em Reais para a moeda de destino.

Args:
valor_reais (float): O valor a ser convertido em Reais.
taxa_destino (float): A taxa de conversão de 1 Real para a moeda de destino.

Returns:
float: O valor convertido na moeda de destino.
"""
return valor_reais * taxa_destino

def main():
"""
Função principal que orquestra a interação com o usuário,
realiza a conversão e exibe o resultado.
"""
print("--- Bem-vindo ao Conversor de Moedas ---")

taxas = obter_taxas_conversao()

while True:
try:
# Solicita o valor em Reais
valor_reais_str = input("\nDigite o valor em Reais (R$): ")
valor_reais = float(valor_reais_str)

if valor_reais < 0:
raise ValueError("O valor em Reais não pode ser negativo.")

# Exibe o menu e solicita a escolha da moeda
exibir_menu_moedas(taxas)
escolha_moeda = input("Digite o número da moeda de destino: ")

# Valida a escolha da moeda
if escolha_moeda not in taxas:
print("Opção de moeda inválida. Por favor, escolha um número da lista.")
continue # Continua o loop para pedir novamente

moeda_selecionada = taxas[escolha_moeda]
nome_moeda = moeda_selecionada["nome"]
taxa = moeda_selecionada["taxa"]

# Realiza a conversão
valor_convertido = converter_moeda(valor_reais, taxa)

# Exibe o resultado
print(f"\n{valor_reais:.2f} Reais equivalem a **{valor_convertido:.2f} {nome_moeda}**
(considerando 1 Real = {taxa} {nome_moeda}).\n")
break # Sai do loop principal após a conversão bem-sucedida

except ValueError as e:
print(f"Erro na entrada: {e}. Por favor, digite um valor numérico válido para o Real.")
except Exception as e:
print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

if __name__ == "__main__":
main()