"""
Criar variáveis para nome(str), idade(int),
altura(float) e peso(float) de uma pessoa
Criar variável com o ano atual(int)
Obter o ano do nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais(peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-strings(com as chaves)
"""

nome = "Jéssica"
idade = 25
altura = 1.65
peso = 50.0
ano_atual = 2020
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')
