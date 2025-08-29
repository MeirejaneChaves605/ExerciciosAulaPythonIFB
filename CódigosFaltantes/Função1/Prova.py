'''''
Questão 4:

Elabore um programa em Python que leia as duas notas de prova (P1 e P2) e duas notas de
trabalho (T1 e T2) e posteriormente exiba a mensagem ‘Aprovado’ ou ‘Não aprovado’
dependendo dos valores obtidos, conforme as regras de cálculo definidas a seguir: • Média de
provas: MP = (P1 + P2)/2 • Média de trabalhos: MT = (T1 + T2)/2 • Média final: MF = 0,8MP +
0,2MT • Situação: ◦ Se MF ≥ 6,0 → aprovado ◦ Se MF < 6,0 → não aprovado, usando função.

'''''

def calcular_media_final(p1, p2, t1, t2):
"""

Calcula a média final do aluno com base nas notas de prova e trabalho.

Args:
p1 (float): Nota da Prova 1.
p2 (float): Nota da Prova 2.
t1 (float): Nota do Trabalho 1.
t2 (float): Nota do Trabalho 2.

Returns:
float: A média final calculada.

Raises:
ValueError: Se alguma nota for negativa ou superior a 10.0.
"""
# Validação de notas: assumindo que notas devem estar entre 0 e 10
for nota in [p1, p2, t1, t2]:
if not (0.0 <= nota <= 10.0):
raise ValueError("Todas as notas (P1, P2, T1, T2) devem estar entre 0.0 e 10.0.")

# Média de provas
mp = (p1 + p2) / 2

# Média de trabalhos
mt = (t1 + t2) / 2

# Média final
mf = (0.8 * mp) + (0.2 * mt)

return mf

def verificar_situacao(media_final):

"""
Verifica a situação do aluno (Aprovado/Não aprovado) com base na média final.

Args:
media_final (float): A média final do aluno.

Returns:
str: 'Aprovado' se a média final for maior ou igual a 6.0,
'Não aprovado' caso contrário.
"""
if media_final >= 6.0:
return "Aprovado"
else:
return "Não aprovado"

def main():
"""
Função principal que gerencia a entrada de notas, calcula a média final
e exibe a situação do aluno.
"""
print("--- Calculadora de Média Final do Aluno ---")
print("Por favor, digite as notas (0.0 a 10.0) a seguir:\n")

while True:
try:
# Leitura das notas de prova
p1 = float(input("Digite a nota da Prova 1 (P1): "))
p2 = float(input("Digite a nota da Prova 2 (P2): "))

# Leitura das notas de trabalho
t1 = float(input("Digite a nota do Trabalho 1 (T1): "))

t2 = float(input("Digite a nota do Trabalho 2 (T2): "))

# Calcula a média final
media_final = calcular_media_final(p1, p2, t1, t2)

# Verifica a situação do aluno
situacao = verificar_situacao(media_final)

print(f"\n--- Resultados ---")
print(f"Média Final (MF): {media_final:.2f}")
print(f"Situação: **{situacao}**")

if situacao == "Aprovado":
print("Parabéns! Você foi aprovado!\n")
else:
print("Que pena! Você não foi aprovado. Estude mais para a próxima!\n")

break # Sai do loop se todas as entradas e cálculos forem válidos

except ValueError as e:
# Captura erros de conversão para float ou validação de notas
print(f"\nErro na entrada: {e}")
print("Por favor, digite valores numéricos entre 0.0 e 10.0 para as notas.\n")
except Exception as e:
# Captura qualquer outro erro inesperado
print(f"\nOcorreu um erro inesperado: {e}. Por favor, tente novamente.\n")

# Garante que a função main() seja executada apenas quando o script for rodado diretamente
if __name__ == "__main__":
main()