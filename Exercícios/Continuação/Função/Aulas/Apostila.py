'''''
Código da apostila de sala.

'''''

nome = input("Digite o nome:")
email = input("digite o email:")
cidade = input("Digite a sua cidade:")

print("\nCadastro realizado com sucesso!\n")

print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"Cidade: {cidade}")

print(f"Nome: {nome}", f"E-mail: {email}", f"Cidade: {cidade}", sep ="\n")
Apostila 2:
senha_correta = "python123"
senha_digitada = ""
contador = 0
print("Digite a senha para acessar o sistema.")
while senha_digitada != senha_correta:
senha_digitada = input("senha:")
if senha_digitada != senha_correta:
contador = contador+1
print("\nSenha incorreta, tente novamente!\n")
if contador < 5:
print("\nAcesso permitido!\n")
else:
print("usuário bloqueado. Número máximo de tentativas é 5. Contate o administrador.")