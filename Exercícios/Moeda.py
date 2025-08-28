'''''
6. Crie um programa em Python que recebe um valor em reais e
o converte para outra moeda. Use um menu para escolher a
moeda de destino:
1. Dólar
2. Euro
3. Libra
4. Iene
O programa deve perguntar o valor em reais e exibir o valor
convertido para a moeda escolhida. Use valores fictícios para
as taxas de conversão:
1 Real = 0.19 Dólar
1 Real = 0.17 Euro
1 Real = 0.15 Libra
1 Real = 25 Ienes

'''''

print("Menu de conversão:")
print("1. Dólar")
print("2. Euro")
print("3. Libra")
print("4. Iene")
opcao = int(input("Escolha a moeda para conversão (1-4): "))
if opcao == 1:
 taxa = 0.19
 moeda = "Dólar"
elif opcao == 2:
 taxa = 0.17
 moeda = "Euro"
elif opcao == 3:
 taxa = 0.15
 moeda = "Libra"
elif opcao == 4:
 taxa = 25
 moeda = "Iene"
else:
 taxa = None
if taxa is not None:
 valor_reais = float(input("Digite o valor em reais (R$): "))
 valor_convertido = valor_reais * taxa
 print(f"{valor_reais:.2f} reais equivalem a {valor_convertido:.2f}
{moeda}")
else:
 print("Opção inválida.")