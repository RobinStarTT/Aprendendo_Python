from rich.traceback import install
install()

#* Enumerate - enumera iteráveis (índices)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)

#? print(lista_enumerada) 
#* O resultado do print é um 'iterator': <enumerate object at 0x00000224698273D0>

#? print(next(lista_enumerada))
#* O resultado desse print é uma tupla: (0, 'Maria') - que contém o índice do nome


#! É possível usar o for com o enumerate

# for item in lista_enumerada:
#     print(item)

#! O primeiro for seria exibido, mas esse segundo debaixo não.
# for item in lista_enumerada:
#     print(item)

#? Após usar um iterator, a lista tem seus valores "consumidos" e se eu quiser puxar
#? novamente esses valores, verificarei que a lista estará vazia.

#? Pra contornar esse problema: usar o enumerate fora da variável

# for item in enumerate(lista):
#     print(item)

# for item in enumerate(lista):
#     print(item)

# for item in enumerate(lista):
#     print(item)

# lista_enumerada_nova = list(enumerate(lista)) 
# #? [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# #*enumera cada item da minha lista, e eu posso controlar em qual índice irá começar
# print(lista_enumerada_nova)

# lista_enumerada_nova = list(enumerate(lista, start=2)) #!aqui o índice irá começar a partir do 2
# print(lista_enumerada_nova)

# for indice, nome in enumerate(lista):
#     print(indice, nome)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)