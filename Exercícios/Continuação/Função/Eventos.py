'''''
Questão 13:

Uma universidade está organizando os dados de participação dos alunos em dois eventos
acadêmicos: uma palestra sobre Inteligência Artificial e um workshop de Programação em
Python. Os dados de presença são armazenados em dois conjuntos distintos: palestra_ia e
workshop_python, contendo os nomes dos alunos que participaram de cada evento. Escreva
um programa em Python com o seguinte menu interativo: 1. Adicionar aluno a um evento: O
programa deve perguntar o nome do aluno e em qual evento ele participou (IA ou Python) e
adicionar o nome ao conjunto correspondente. 2. Mostrar alunos que participaram de ambos
os eventos: Exiba os nomes que aparecem nos dois conjuntos (interseção). 3. Mostrar alunos
que participaram somente da palestra de IA: Exiba os nomes que estão no conjunto da
palestra, mas não no workshop (diferença). 4. Mostrar alunos que participaram de pelo menos
um evento: Exiba a união dos dois conjuntos, sem repetições. 5. Verificar participação de um
aluno: Solicite o nome de um aluno e diga se ele participou de ambos, somente um ou nenhum
dos eventos. 6. Sair O programa deve funcionar em laço até que o usuário escolha a opção de
sair. Utilize operações com conjuntos (union, intersection, difference) para resolver as tarefas.
Utilizar função.

'''''

def get_user_info():
"""
Asks the user for their name and age.

Returns:
tuple: A tuple containing the user's name (str) and age (int).
"""
name = input("Hi there! What's your name? ").strip()

while True:
try:
age_str = input(f"Nice to meet you, {name}! How old are you? ").strip()
age = int(age_str)
if age <= 0:
print("Your age must be a positive number. Please try again.")
else:
break
except ValueError:
print("That doesn't look like a valid age. Please enter a whole number.")

return name, age

def print_greeting(name, age):
"""
Prints a personalized greeting using the provided name and age.

Args:
name (str): The name of the user.
age (int): The age of the user.
"""
print(f"\nHello, {name}! It's great to know you are {age} years old.")
if age < 18:
print("You're still quite young!")
elif age >= 18 and age < 60:
print("Hope you're having a productive time!")

else:
print("Wisdom comes with age!")

def main():
"""
Main function to run the greeting program.
"""
print("--- Welcome to the Greeting Program! ---")

# Get user information using a function
user_name, user_age = get_user_info()

# Print the greeting using another function
print_greeting(user_name, user_age)

print("\n--- Program finished. Have a great day! ---")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
main()