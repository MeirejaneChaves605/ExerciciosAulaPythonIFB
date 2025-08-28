'''''
Questão 15:

Você foi contratado para desenvolver um sistema simples para gerenciar um campeonato de
futebol. O sistema deve usar um dicionário onde as chaves são os nomes dos times e os
valores são os pontos conquistados. O programa deve apresentar o seguinte menu: 1.
Adicionar time: permite cadastrar um novo time com 0 pontos iniciais. 2. Registrar resultado
de partida: o usuário informa os nomes de dois times e o resultado da partida (quantidade de
gols de cada time). O programa atualiza os pontos dos times: 3 pontos para o vencedor, 1
ponto para empate, 0 para o perdedor. 3. Mostrar classificação: exibe a lista dos times e seus
pontos, ordenada do maior para o menor número de pontos. 4. Remover time: permite

remover um time da competição. 5. Sair O programa deve funcionar em loop até o usuário
escolher sair. Utilizar função.

'''''

def adicionar_time(campeonato):
"""
Adiciona um novo time ao campeonato com 0 pontos iniciais.
Impede a adição de times com nomes duplicados.
"""
nome_time = input("\nDigite o nome do novo time: ").strip().title()
if nome_time in campeonato:
print(f"O time '{nome_time}' já está cadastrado no campeonato.")
else:
campeonato[nome_time] = 0 # Novo time começa com 0 pontos
print(f"Time '{nome_time}' adicionado com sucesso!")

def registrar_resultado(campeonato):
"""
Registra o resultado de uma partida e atualiza os pontos dos times.
Valida a existência dos times e os gols.
"""
if len(campeonato) < 2:
print("\nSão necessários pelo menos dois times para registrar uma partida.")
return

print("\n--- Registrar Resultado de Partida ---")
time1 = input("Digite o nome do primeiro time: ").strip().title()
time2 = input("Digite o nome do segundo time: ").strip().title()

if time1 not in campeonato:
print(f"Erro: Time '{time1}' não encontrado no campeonato.")
return

if time2 not in campeonato:
print(f"Erro: Time '{time2}' não encontrado no campeonato.")
return
if time1 == time2:
print("Erro: Os times devem ser diferentes.")
return

while True:
try:
gols_time1_str = input(f"Quantos gols o '{time1}' marcou? ")
gols_time1 = int(gols_time1_str)
if gols_time1 < 0:
print("Número de gols não pode ser negativo.")
continue

gols_time2_str = input(f"Quantos gols o '{time2}' marcou? ")
gols_time2 = int(gols_time2_str)
if gols_time2 < 0:
print("Número de gols não pode ser negativo.")
continue
break
except ValueError:
print("Entrada inválida. Por favor, digite um número inteiro para os gols.")

# Atualiza os pontos
if gols_time1 > gols_time2:
campeonato[time1] += 3
print(f"\n{time1} venceu a partida! {time1} ganhou 3 pontos.")
elif gols_time2 > gols_time1:
campeonato[time2] += 3
print(f"\n{time2} venceu a partida! {time2} ganhou 3 pontos.")

else:
campeonato[time1] += 1
campeonato[time2] += 1
print(f"\nPartida empatada! {time1} e {time2} ganharam 1 ponto cada.")

def mostrar_classificacao(campeonato):
"""
Exibe a classificação dos times, ordenada do maior para o menor número de pontos.
"""
if not campeonato:
print("\nNão há times cadastrados no campeonato ainda.")
return

print("\n--- CLASSIFICAÇÃO DO CAMPEONATO ---")
# Ordena os itens do dicionário pelos valores (pontos) em ordem decrescente
# Se os pontos forem iguais, a ordem alfabética do nome do time (chave) será usada
times_ordenados = sorted(campeonato.items(), key=lambda item: item[1], reverse=True)

for time, pontos in times_ordenados:
print(f"- {time}: {pontos} pontos")
print("-----------------------------------\n")

def remover_time(campeonato):
"""
Remove um time da competição.
"""
if not campeonato:
print("\nNão há times cadastrados para remover.")
return

nome_time_remover = input("\nDigite o nome do time que deseja remover: ").strip().title()

if nome_time_remover in campeonato:
del campeonato[nome_time_remover]
print(f"Time '{nome_time_remover}' removido do campeonato.")
else:
print(f"Time '{nome_time_remover}' não encontrado no campeonato.")

def exibir_menu():
"""
Exibe as opções do menu principal do sistema.
"""
print("\n--- MENU DO CAMPEONATO DE FUTEBOL ---")
print("1. Adicionar time")
print("2. Registrar resultado de partida")
print("3. Mostrar classificação")
print("4. Remover time")
print("5. Sair")
print("--------------------------------------")

def main():
"""
Função principal que gerencia o fluxo do programa.
"""
times_campeonato = {} # Dicionário para armazenar os times e seus pontos

print("Bem-vindo ao Gerenciador de Campeonato de Futebol!")

while True:
exibir_menu()
opcao = input("Escolha uma opção: ").strip()

if opcao == '1':

adicionar_time(times_campeonato)
elif opcao == '2':
registrar_resultado(times_campeonato)
elif opcao == '3':
mostrar_classificacao(times_campeonato)
elif opcao == '4':
remover_time(times_campeonato)
elif opcao == '5':
print("Saindo do Gerenciador de Campeonato. Até a próxima!")
break
else:
print("Opção inválida. Por favor, escolha um número de 1 a 5.")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()