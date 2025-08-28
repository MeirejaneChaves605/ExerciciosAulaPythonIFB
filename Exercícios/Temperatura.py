'''''
5. Faça um programa em Python que leia a temperatura em
graus Celsius e determine a classificação da temperatura:
 • Menor que 0°C: Frio extremo
 • De 0°C a 10°C: Frio
 • De 11°C a 25°C: Ameno
 • De 26°C a 35°C: Quente
 • Maior que 35°C: Muito quente

 '''''
# lê a temperatura em graus Celsius
temperatura = float(input("Digite a temperatura em °C: "))
# classificação da temperatura
if temperatura < 0:
 print("Frio extremo")
elif 0 <= temperatura <= 10:
 print("Frio")
elif 11 <= temperatura <= 25:
 print("Ameno")
elif 26 <= temperatura <= 35:
 print("Quente")
else:
 print("Muito quente")