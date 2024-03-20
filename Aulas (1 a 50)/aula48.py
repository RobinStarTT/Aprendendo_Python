"""
Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices de fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

#         0    1        2          3    4
#        -5   -4       -3         -2   -1
lista = [123, True, 'Luiz Otávio', 1.2, []]

lista[-3] = 'Maria'

print(lista)
print(lista[2], type(lista[2]))