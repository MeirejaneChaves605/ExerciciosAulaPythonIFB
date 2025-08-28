'''
14. Uma livraria quer controlar seu estoque usando um
dicionário onde as chaves são os títulos dos livros e os
valores são a quantidade disponível em estoque. Implemente
um programa com as seguintes funcionalidades:
1. Adicionar um livro ao estoque: o usuário informa o título e a
quantidade (se o livro já existir, some a quantidade nova à
existente).
2. Remover unidades de um livro: o usuário informa o título e
a quantidade a remover; o programa deve atualizar o estoque
e avisar se o estoque ficar zerado ou se o livro não existir.
3. Consultar quantidade de um livro: o usuário digita o título e
o programa mostra a quantidade disponível ou informa que o
livro não está no estoque.
4. Mostrar todos os livros com suas quantidades ordenados
alfabeticamente.
5. Sair
O programa deve repetir o menu até que o usuário escolha
sair. Utilizar função.

'''

estoque = {}
def adicionar_livro():
 titulo = input("Título do livro: ").strip()
 qtd = int(input("Quantidade a adicionar: "))
 if titulo in estoque:
 estoque[titulo] += qtd
 else:
 estoque[titulo] = qtd
 print(f"{qtd} unidade(s) de '{titulo}' adicionada(s).")
def remover_livro():
 titulo = input("Título do livro: ").strip()
 if titulo not in estoque:
 print("Livro não encontrado no estoque.")
 return
 qtd = int(input("Quantidade a remover: "))
 if qtd > estoque[titulo]:
 print(f"Não há unidades suficientes para remover. Estoque atual:
{estoque[titulo]}")
 return
 estoque[titulo] -= qtd
 print(f"{qtd} unidade(s) removida(s) de '{titulo}'.")
 if estoque[titulo] == 0:
 print(f"Estoque do livro '{titulo}' zerado.")
def consultar_livro():
 titulo = input("Título do livro: ").strip()
 if titulo in estoque:
 print(f"Quantidade disponível de '{titulo}': {estoque[titulo]}")
 else:
 print("Livro não está no estoque.")
def mostrar_estoque():
 if not estoque:
 print("Estoque vazio.")
 return
 print("\nLivros em estoque:")
 for titulo in sorted(estoque.keys()):
 print(f"{titulo}: {estoque[titulo]}")
def menu():
 while True:
 print("\n--- MENU ---")
 print("1. Adicionar livro ao estoque")
 print("2. Remover unidades de um livro")
 print("3. Consultar quantidade de um livro")
 print("4. Mostrar todos os livros com quantidades")
 print("5. Sair")
 opcao = input("Escolha uma opção: ").strip()
 if opcao == '1':
 adicionar_livro()
 elif opcao == '2':
 remover_livro()
 elif opcao == '3':
 consultar_livro()
 elif opcao == '4':
 mostrar_estoque()
 elif opcao == '5':
 print("Encerrando o programa.")
 break
 else:
 print("Opção inválida, tente novamente.")
def main():
 menu()
if __name__ == "__main__":
 main()
