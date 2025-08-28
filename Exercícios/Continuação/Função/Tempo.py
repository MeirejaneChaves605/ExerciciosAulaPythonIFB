
'''''
Faça um programa em Python que leia a temperatura em graus Celsius e determine a
classificação da temperatura: • Menor que 0°C: Frio extremo • De 0°C a 10°C: Frio • De 11°C a
25°C: Ameno • De 26°C a 35°C: Quente • Maior que 35°C: Muito quente, usando função.

'''''

def classificar_temperatura(temperatura_celsius):
"""
Classifica a temperatura em graus Celsius de acordo com categorias predefinidas.

Args:
temperatura_celsius (float): A temperatura em graus Celsius.

Returns:
str: A classificação da temperatura.
"""
if temperatura_celsius < 0:
return "Frio extremo"
elif 0 <= temperatura_celsius <= 10:
return "Frio"
elif 11 <= temperatura_celsius <= 25:
return "Ameno"
elif 26 <= temperatura_celsius <= 35:
return "Quente"
else: # temperatura_celsius > 35
return "Muito quente"

def main():
"""
Função principal que solicita a temperatura ao usuário,
classifica-a e exibe o resultado.
"""
print("--- Classificador de Temperatura ---")
print("Vamos classificar a temperatura em graus Celsius.")

while True:
try:
# Solicita a temperatura ao usuário
temperatura_str = input("\nDigite a temperatura em graus Celsius (°C): ")
temperatura_celsius = float(temperatura_str)

# Chama a função para classificar a temperatura
classificacao = classificar_temperatura(temperatura_celsius)

# Exibe o resultado
print(f"A temperatura de {temperatura_celsius:.1f}°C é classificada como:
**{classificacao}**\n")
break # Sai do loop se a entrada for válida

except ValueError:
# Captura erros se o usuário não digitar um número válido
print("Entrada inválida. Por favor, digite um valor numérico para a temperatura.\n")
except Exception as e:
# Captura qualquer outro erro inesperado
print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.\n")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":

main()