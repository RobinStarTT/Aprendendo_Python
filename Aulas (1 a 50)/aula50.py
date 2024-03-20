from rich.traceback import install

# Instalar o traceback aprimorado
install()

# Seu código aqui

"""
Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices de fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create, read, update, delete (CRUD)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b 
# lista_a.extend(lista_b)
# print(lista_a)

'''
# * Exercício: Exiba os índices da lista:
# * lista = ['Maria', 'Helena', 'Luiz']
'''
'''
# * Minha resolução:
contador = 0

lista = ['Maria', 'Helena', 'Luiz']
for nome in lista:
    print ('Nome: ',nome, '. Índice respectivo: ',contador)
    contador += 1
'''


# * Resolução do professor:

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))


#
# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'Joao'\

# print(nome)
# print(noutra_variavel)



# lista_a = ['Luiz', 'Maria']
# lista_b = lista_a.copy() #copia a lista A da forma como ela está, e se a lista A for alterada, essa alteração não aparecerá na lista B.

# lista_a[0] = 'Qualquer coisa'

# print(lista_b)

# TODO - for in com listas

lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print (nome, type(nome))