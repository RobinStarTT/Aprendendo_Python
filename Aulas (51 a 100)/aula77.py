import copy
"""
Métodos úteis para dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda 3',
#     #'idade' : 900,
# }
# pessoa.setdefault('idade', None) #criar um item no dicionário e colocar um valor padrão neste item
# pessoa.setdefault('idade', 0) #criar um item no dicionário e colocar um valor padrão neste item
# #todo caso exista a chave e o seu valor, a linha do setdefault não precisará funcionar
# print(pessoa['idade'])
# # print(len(pessoa)) #!quantas chaves tem no dicionário

# print(list(pessoa.keys())) #!mostra as chaves e converte-as para uma lista por type conversion

# # for chave in pessoa.keys():
# #     print(chave)
# # #!ou
# # for chave in pessoa:
# #     print(chave)


# print(list(pessoa.values())) #!mostra os valores de cada chave e converte-os para uma lista por type conversion

# for valor in pessoa.values():
#     print(valor)

# print(list(pessoa.items())) #!printa na tela a chave e o seu valor correspondente no formato de lista com tuplas


# for chave, valor in pessoa.items(): #!printa separadamente chave e valor
#     print(chave, valor)

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }

# d2 = d1.copy() #!copia o outro dicionário e separa suas propriedades
# #todo mas é uma cópia rasa porque se tiver algum valor mutável dentro do dicionário, este valor não será propriamente copiado, ele será somente
# #todo linkado na outra lista
# #todo caso eu queira uma cópia real e precisa, eu posso usar uma biblioteca do python chamada de deepcopy (cópia profunda)
# #!import copy


# d2['c1'] = 1000
# d2['l1'][1] = 99999 #!alterando a lista dentro do dicionário, mesmo tendo feito o copy dos dicts, o que é mutável como listas não são separadas e sim
# #!compartilhadas
# print(d1)
# print(d2)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = copy.deepcopy(d1) #!copia tudo inclusive os dados mutáveis com uma cópia profunda

d2['c1'] = 1000
d2['l1'][1] = 99999 
print(d1)
print(d2)

d2 = copy.deepcopy(d1)





