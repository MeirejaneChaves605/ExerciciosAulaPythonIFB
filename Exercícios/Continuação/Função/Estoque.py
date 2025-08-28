'''''
Uma livraria quer controlar seu estoque usando um dicionário onde as chaves são os títulos
dos livros e os valores são a quantidade disponível em estoque. Implemente um programa com
as seguintes funcionalidades: 1. Adicionar um livro ao estoque: o usuário informa o título e a
quantidade (se o livro já existir, some a quantidade nova à existente). 2. Remover unidades de
um livro: o usuário informa o título e a quantidade a remover; o programa deve atualizar o
estoque e avisar se o estoque ficar zerado ou se o livro não existir. 3. Consultar quantidade de
um livro: o usuário digita o título e o programa mostra a quantidade disponível ou informa que
o livro não está no estoque. 4. Mostrar todos os livros com suas quantidades ordenados
alfabeticamente. 5. Sair O programa deve repetir o menu até que o usuário escolha sair.
Utilizar função.

'''''

def adicionar_livro(estoque):
"""
Adiciona um novo livro ao estoque ou soma a quantidade se o livro já existir.
"""
titulo = input("\nDigite o título do livro: ").strip().title() # .title() capitaliza a primeira letra de
cada palavra
while True:
try:
quantidade_str = input(f"Digite a quantidade de '{titulo}' a adicionar: ")
quantidade = int(quantidade_str)
if quantidade <= 0:
print("A quantidade deve ser um número positivo. Tente novamente.")
else:
break
except ValueError:
print("Entrada inválida. Por favor, digite um número inteiro para a quantidade.")

if titulo in estoque:
estoque[titulo] += quantidade
print(f"Quantidade de '{titulo}' atualizada. Novo estoque: {estoque[titulo]} unidades.")
else:
estoque[titulo] = quantidade
print(f"Livro '{titulo}' adicionado ao estoque com {quantidade} unidades.")

def remover_unidades(estoque):
"""
Remove unidades de um livro existente no estoque.
Avisa se o estoque ficar zerado ou se o livro não existir.
"""
if not estoque:
print("\nO estoque está vazio. Não há livros para remover unidades.")
return

titulo = input("\nDigite o título do livro para remover unidades: ").strip().title()

if titulo not in estoque:
print(f"Livro '{titulo}' não encontrado no estoque.")
return

while True:
try:
quantidade_remover_str = input(f"Digite a quantidade a remover de '{titulo}' (Estoque
atual: {estoque[titulo]}): ")
quantidade_remover = int(quantidade_remover_str)
if quantidade_remover <= 0:
print("A quantidade a remover deve ser um número positivo. Tente novamente.")
elif quantidade_remover > estoque[titulo]:
print(f"Quantidade insuficiente em estoque para '{titulo}'. Disponível:
{estoque[titulo]} unidades.")
else:
break
except ValueError:
print("Entrada inválida. Por favor, digite um número inteiro para a quantidade a
remover.")

estoque[titulo] -= quantidade_remover

if estoque[titulo] == 0:
print(f"Todas as {quantidade_remover} unidades de '{titulo}' foram removidas. O estoque
deste livro está ZERADO.")
del estoque[titulo] # Remove o livro do dicionário se o estoque for 0
else:
print(f"{quantidade_remover} unidades de '{titulo}' removidas. Novo estoque:
{estoque[titulo]} unidades.")

def consultar_quantidade(estoque):
"""
Consulta e exibe a quantidade disponível de um livro.
"""
titulo = input("\nDigite o título do livro para consultar: ").strip().title()

if titulo in estoque:
print(f"A quantidade disponível de '{titulo}' é: {estoque[titulo]} unidades.")
else:
print(f"Livro '{titulo}' não encontrado no estoque.")

def mostrar_todos_livros(estoque):
"""
Exibe todos os livros no estoque com suas quantidades, ordenados alfabeticamente.
"""
if not estoque:
print("\nO estoque está vazio.")
return

print("\n--- ESTOQUE ATUAL DA LIVRARIA (Ordenado Alfabeticamente) ---")
# Ordena os itens do dicionário pelas chaves (títulos)
for titulo, quantidade in sorted(estoque.items()):
print(f"- {titulo}: {quantidade} unidades")
print("----------------------------------------------------------\n")

def exibir_menu():
"""
Exibe as opções do menu principal do programa.
"""
print("\n--- MENU DE ESTOQUE DA LIVRARIA ---")
print("1. Adicionar um livro ao estoque")
print("2. Remover unidades de um livro")
print("3. Consultar quantidade de um livro")
print("4. Mostrar todos os livros com suas quantidades")
print("5. Sair")
print("-----------------------------------")

def main():
"""
Função principal que gerencia o fluxo do programa.
"""
estoque_livraria = {} # Dicionário para armazenar o estoque

print("Bem-vindo ao Sistema de Gerenciamento de Estoque da Livraria!")

while True:
exibir_menu()
opcao = input("Escolha uma opção: ").strip()

if opcao == '1':
adicionar_livro(estoque_livraria)
elif opcao == '2':
remover_unidades(estoque_livraria)
elif opcao == '3':
consultar_quantidade(estoque_livraria)

elif opcao == '4':
mostrar_todos_livros(estoque_livraria)
elif opcao == '5':
print("Saindo do sistema de estoque. Até logo!")
break
else:
print("Opção inválida. Por favor, escolha um número de 1 a 5.")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()