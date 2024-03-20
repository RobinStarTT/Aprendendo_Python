from rich.traceback import install
install()

#*Lista de listas e seus índices

# salas = [
#     #!0          1
#     ['Maria', 'Helena', ],         #*0
#     #!0
#     ['Elaine', ],                  #*1
#     #!0          1       2
#     ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], #*2

# ]
#? forma de acessar a lista de índice 1 dentro da lista maior
# print(salas[1])

#? para acessar o índice de uma lista dentro de outra lista seria:
# print(salas[1][0])
# #!aqui eu acesso a lista de índice 1, e o item dentro dessa lista de índice 0
# #*resultado do print é: Elaine

# #?buscando o valor Helena na lista de índice 0:
# print(salas[0][1])

# #?buscando o valor Eduarda na lista de índice 2:
# print(salas[2][2])

# #?buscando o valor 20 da tupla que está na lista de índice 2 da lista maior:
# print(salas[2][3][2])

salas = [
    #!0          1
    ['Maria', 'Helena', ],         #*0
    #!0
    ['Elaine', ],                  #*1
    #!0          1       2
    ['Luiz', 'João', 'Eduarda', ], #*2

]

for sala in salas: #!esse for maior pega as listas maiores que contêm os nomes dos alunos
    print(f'A sala é {sala}')
    for aluno in sala: #!esse for menor pega especificamente os nomes dos alunos
        print(aluno)





