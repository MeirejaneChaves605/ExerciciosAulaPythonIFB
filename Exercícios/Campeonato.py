'''''
15. Você foi contratado para desenvolver um sistema simples
para gerenciar um campeonato de futebol. O sistema deve
usar um dicionário onde as chaves são os nomes dos times e
os valores são os pontos conquistados. O programa deve
apresentar o seguinte menu:
1. Adicionar time: permite cadastrar um novo time com 0
pontos iniciais.
2. Registrar resultado de partida: o usuário informa os nomes
de dois times e o resultado da partida (quantidade de gols de
cada time). O programa atualiza os pontos dos times: 3
pontos para o vencedor, 1 ponto para empate, 0 para o
perdedor.
3. Mostrar classificação: exibe a lista dos times e seus
pontos, ordenada do maior para o menor número de pontos.
4. Remover time: permite remover um time da competição.
5. Sair
O programa deve funcionar em loop até o usuário escolher
sair. Utilizar função.

'''''

campeonato = {}
def adicionar_time():
 time = input("Nome do time a adicionar: ").strip()
 if time in campeonato:
 print("Este time já está cadastrado.")
 else:
 campeonato[time] = 0
 print(f"Time '{time}' adicionado com 0 pontos.")
def registrar_resultado():
 time1 = input("Nome do primeiro time: ").strip()
 time2 = input("Nome do segundo time: ").strip()
 if time1 not in campeonato or time2 not in campeonato:
 print("Ambos os times devem estar cadastrados.")
 return
 gols1 = int(input(f"Gols do {time1}: "))
 gols2 = int(input(f"Gols do {time2}: "))
 if gols1 > gols2:
 campeonato[time1] += 3
 print(f"{time1} venceu e ganhou 3 pontos.")
 elif gols2 > gols1:
 campeonato[time2] += 3
 print(f"{time2} venceu e ganhou 3 pontos.")
 else:
 campeonato[time1] += 1
 campeonato[time2] += 1
 print("Empate. Cada time ganhou 1 ponto.")
def obter_pontos(item):
 return item[1]
def mostrar_classificacao():
 if not campeonato:
 print("Nenhum time cadastrado.")
 return
 print("\nClassificação:")
 ordenado = sorted(campeonato.items(), key=obter_pontos,
reverse=True)
 for time, pontos in ordenado:
 print(f"{time}: {pontos} ponto(s)")
def remover_time():
 time = input("Nome do time a remover: ").strip()
 if time in campeonato:
 del campeonato[time]
 print(f"Time '{time}' removido do campeonato.")
 else:
 print("Time não encontrado.")
def menu():
 while True:
 print("\n--- MENU DO CAMPEONATO ---")
 print("1. Adicionar time")
 print("2. Registrar resultado de partida")
 print("3. Mostrar classificação")
 print("4. Remover time")
 print("5. Sair")
 opcao = input("Escolha uma opção: ").strip()
 if opcao == '1':
 adicionar_time()
 elif opcao == '2':
 registrar_resultado()
 elif opcao == '3':
 mostrar_classificacao()
 elif opcao == '4':
 remover_time()
 elif opcao == '5':
 print("Encerrando o programa.")
 break
 else:
 print("Opção inválida. Tente novamente.")
def main():
 menu()
if __name__ == "__main__":
 main()