"""
Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices de fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create, read, update, delete (CRUD)
Criar, ler, alterar, apagar = lista[i] (CRUD)
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

#for in com listas

# lista = ['Maria', 'Helena', 'Luiz']

# for nome in lista:
#     print(nome, type(nome))

# lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# lista_b = lista_a.copy()

# lista_a[0] = 'Qualquer coisa'
# print(lista_a)
# print(lista_b)

# #         0    1        2          3    4
# #        -5   -4       -3         -2   -1
# lista = [123, True, 'Luiz Otávio', 1.2, []]

# lista[-3] = 'Maria'

# print(lista)
# print(lista[2], type(lista[2]))

#         0   1   2   3   4   5 
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50) #acrescenta na lista
lista.pop()
lista.append(60)
lista.append(70)
lista.pop()
ultimo_valor = lista.pop(3)
print(lista, 'Removido, ', ultimo_valor)


