"""
Iterando strings com while
"""

nome = 'Luiz Otávio' #Iteráveis

contador = 0

novo_nome = '*'

while contador < len(nome):
    letra = nome[contador]
    print(letra)
    novo_nome += letra + '*'
    contador += 1

print(novo_nome)
