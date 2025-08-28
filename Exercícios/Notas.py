'''''
4. Elabore um programa em Python que leia as duas notas de
prova (P1 e P2) e duas notas de trabalho (T1 e T2) e
posteriormente exiba a mensagem 'Aprovado' ou 'Não
aprovado' dependendo dos valores obtidos, conforme as
regras de cálculo definidas a seguir:
 • Média de provas: MP = (P1 + P2)/2
 • Média de trabalhos: MT = (T1 + T2)/2
 • Média final: MF = 0,8MP + 0,2MT
 • Situação:
 ◦ Se MF ≥ 6,0 → aprovado
 ◦ Se MF < 6,0 → não aprovado
 
 '''''
# leitura das notas
P1 = float(input("Digite a nota da prova 1 (P1): "))
P2 = float(input("Digite a nota da prova 2 (P2): "))
T1 = float(input("Digite a nota do trabalho 1 (T1): "))
T2 = float(input("Digite a nota do trabalho 2 (T2): "))
# cálculo das médias
MP = (P1 + P2) / 2
MT = (T1 + T2) / 2
MF = 0.8 * MP + 0.2 * MT
# verificação da situação
if MF >= 6.0:
 print("Aprovado")
else:
 print("Não aprovado")