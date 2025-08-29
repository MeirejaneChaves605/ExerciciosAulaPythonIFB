'''''
Questão 3:

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).

'''''

def calcular_tempo_download(tamanho_mb, velocidade_mbps):
"""
Calcula o tempo aproximado de download de um arquivo.

Args:
tamanho_mb (float): O tamanho do arquivo em Megabytes (MB).
velocidade_mbps (float): A velocidade do link de Internet em Megabits por segundo
(Mbps).

Returns:
float: O tempo aproximado de download em minutos.

Raises:
ValueError: Se o tamanho do arquivo ou a velocidade do link forem não positivos.
"""
if tamanho_mb <= 0:
raise ValueError("O tamanho do arquivo deve ser um valor positivo.")
if velocidade_mbps <= 0:
raise ValueError("A velocidade do link de Internet deve ser um valor positivo.")

# 1 byte = 8 bits
# 1 Megabyte (MB) = 8 Megabits (Mb)
# Para converter MB para Mb, multiplicamos por 8.
tamanho_mbits = tamanho_mb * 8

# Tempo em segundos = Tamanho em Mbits / Velocidade em Mbps
tempo_segundos = tamanho_mbits / velocidade_mbps

# Converter segundos para minutos
tempo_minutos = tempo_segundos / 60

return tempo_minutos

def main():
"""
Função principal que interage com o usuário para obter os dados
e exibir o tempo de download calculado.
"""
print("--- Calculadora de Tempo de Download ---")
print("Vamos calcular quanto tempo levará para baixar seu arquivo.")

while True:
try:
# Solicita o tamanho do arquivo
tamanho_mb_str = input("\nDigite o tamanho do arquivo para download (em MB): ")
tamanho_mb = float(tamanho_mb_str)

# Solicita a velocidade da internet
velocidade_mbps_str = input("Digite a velocidade do seu link de Internet (em Mbps): ")
velocidade_mbps = float(velocidade_mbps_str)

# Chama a função para calcular o tempo de download
tempo_minutos = calcular_tempo_download(tamanho_mb, velocidade_mbps)

# Imprime o resultado formatado
print(f"\nTempo aproximado de download: {tempo_minutos:.2f} minutos.\n")
break # Sai do loop se tudo ocorreu bem

except ValueError as e:
# Captura erros de conversão para float ou validação da função de cálculo
print(f"Erro na entrada: {e}. Por favor, digite valores numéricos positivos.")
except Exception as e:

# Captura qualquer outro erro inesperado
print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()