
#todo manipulando as chaves e valores em dicionários:

pessoa = {}
pessoa_2 = {}
#todo criando uma chave num dicionário:

pessoa['nome'] = 'Luiz Otávio'

print(pessoa)
print(pessoa['nome'])

#todo chaves dinâmicas:
chave = 'nome'
pessoa_2[chave] = 'Luiz Otávio'

print(pessoa_2[chave])
print(pessoa)

pessoa['sobrenome'] = 'Miranda'

#todo apagando uma chave do dicionário:

del pessoa['sobrenome']
print(pessoa)



# #todo tentar buscar uma chave que não exista:
# if pessoa.get('sobrenome', None): #!usa o método .get para pegar essa chave (se existir) - se não existir, posso passar um valor padrão no 
#     print('EXISTE') #!lugar de 'None'


# if pessoa.get('sobrenome', 'Não existe'):
#     print('existe')

#*corrigido então

if pessoa.get('sobrenome') is None:
    print('Não existe')

else:
    print(pessoa['sobrenome'])





