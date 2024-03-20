"""
*Dicionários em Python (tipo dict)
São estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como "índices" que vimos na lista e podem ser de tipos imutáveis como:
str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
?Usamos as chaves - {} - ou a classe dict para criar dicionários.
!Imutáveis: str, int, float, bool, tuple
!Mutáveis: dict, list
"""

pessoa = {
    'nome': 'Luiz Otávio', #?usa-se 2 pontos (:) no dicionário e não igual (=)
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
print(pessoa, type(pessoa))

print(pessoa['nome']) #?aceso ao valor da chave nome, no caso, Luiz Otávio
#!igual a lista, só que o índice é definido pelo programador
#!o dicionário não é iterável, mas ele pode imprimir as chaves

for chave in pessoa: #!imprime os índices
    print(chave)

for chave in pessoa: #!imprime os índices e valores
    print(chave, pessoa[chave])






