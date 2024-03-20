from rich.traceback import install
install()

#*Desempacotamento em chamadas de métodos e funções

# string = 'ABCD'
# lista = ['Maria', 'Helena', 'Eduarda']
# tupla = 'Python', 'é', 'legal'

# a, b, c = lista
# print(a, c)

#!exemplo de desempacotamento:


string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #!0          1
    ['Maria', 'Helena', ],         #*0
    #!0
    ['Elaine', ],                  #*1
    #!0          1       2
    ['Luiz', 'João', 'Eduarda', ], #*2

]

# #todo o *_ serve para representar o intervalo que não será usado
# a, b, *_, c, d = lista 
# print(a, d)

# #? a = começo da lista; d = fim da lista // assim eu consigo determinar onde está a informação que eu desejo

# for nome in lista:
#     print(nome, end=' ')

#!outra forma de desempacotar os dados de uma lista é:

# print(*lista)
# print(*string) #!passa cada um dos itens da string 'string' pela a função print
# print(*tupla)

print(*salas, end ='\n') #!quebra de linha no fim da lista
print(*salas, sep = '\n') #!quebra de linha após o fim de cada lista


