'''''
3. Faça um programa que peça o tamanho de um arquivo para
download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).

'''''

# lê o tamanho do arquivo em MB
tamanho_arquivo = float(input("Digite o tamanho do arquivo para
download (MB): "))
# lê a velocidade do link em Mbps
velocidade_link = float(input("Digite a velocidade do link de Internet
(Mbps): "))
# converte a velocidade para MBps (Megabytes por segundo)
# 1 byte = 8 bits, então MBps = Mbps / 8
velocidade_MBps = velocidade_link / 8
# calcula o tempo em segundos
tempo_segundos = tamanho_arquivo / velocidade_MBps
# converte para minutos
tempo_minutos = tempo_segundos / 60
# imprime o resultado
print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")