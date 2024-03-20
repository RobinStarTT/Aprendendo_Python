from rich.traceback import install
install()

# #* split e join com list e str
# #* split - divide uma string (list)
# #* join - une uma string

# frase = '         Olha só que, coisa interessante           '
# lista_palavras = frase.split(',')

# #todo editando a própria lista usando valores que ela mesmo gerou pelo método split
# for i, frase in enumerate(lista_palavras):
#     # print(lista_palavras[i]) #* ou
#     print(lista_palavras[i].strip()) #*corta os espaços do começo e do fim da string
#     #!ou ainda, é possível alterar o índice da lista e podar os espaços que tem na lista:
#     lista_palavras[i] = lista_palavras[i].strip() #!o valor do índice 'i' é o mesmo valor do índice com o método strip
# print(lista_palavras)
#     #!pois a lista é mutável enquanto a string por si só não o é
#     #!alterando a própria lista
# #todo existe o rstrip (right strip - corta os espaços da direita) - e tem o lstrip (left strip - corta os espaços da esquerda)

# # print(lista_palavras) #* gera uma lista sendo cada item dessa lista as palavras dentro da string

# # #!caso eu queira dividir a string a partir de algo dentro dela, eu posso, por exemplo usar a vírgula que contém na variável 'frase'

# # lista_palavras_separadas = frase.split(',')
# # print(lista_palavras_separadas)

# # #!ou é possível fazer dessa seguinte forma também: 

# # lista_palavras_separadas_2 = frase.split(', ')
# # print(lista_palavras_separadas_2)


# #? a melhor cois a se fazer então é criar uma nova lista com os dados corretos, ex:
frase = '         Olha só que        , coisa interessante           '
lista_frases_cruas = frase.split(',')

lista_frases_fixed = []

# for i, frase in enumerate(lista_frases_cruas):
#     lista_frases_fixed.append(lista_frases_cruas[i].strip())
# # print(lista_frases_fixed) #!criei uma nova lista com os dados formatados da lista anterior (boa prática)
# # #*pois em outro momento do código pode ser necessário voltar na lista inicial.
    
# frases_unidas = '-'.join('abc') #!join é um método da string e não da lista
#? resultado: abc
#? agora se for frases_unidas = '-'.join('abc')
#* resultado: a-b-c
#! é possível dar join em lista, tupla, strings o que for, desde que seja um iterável
frases_unidas = '-'.join(lista_frases_fixed) #!join é um método da string e não da lista

print(frases_unidas)




