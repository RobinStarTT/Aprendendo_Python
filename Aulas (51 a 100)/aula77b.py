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

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# print(p1.get('nome', 'Não existe')) #!obter o valor da chave nome
# #todo se a chave e o seu valor não existisse, o print seria de 'None'.

# nome = p1.pop('nome')
# print(nome)
# print(p1) #!apagou o nome e o seu valor

# ultima_chave = p1.popitem() #!apagou a última chave do dicionário
# print(ultima_chave)



# p1.update({ #!atualiza uma chave e não mexe nas outras
#     'nome': 'novo valor'
#     'idade': 30, #!atualiza as chaves existentes e cria outras também
# })
# print(p1)

#!posso passar argumentos não nomeados também

# p1.update(nome='novo valor', idade = 30) #!não precisa escrever as chaves como strings, já passa os valores e as chaves automaticamente
# print(p1)


tupla = ('nome', 'novo valor'), ('idade', 30)#!sempre deixar uma vírgula sobrando na tupla
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(tupla) #? e p1.update(lista) dá no mesmo resultado // 
#!iterável que dentro dele mesmo há outro iterável (ou seja, 2 valores: chave e valor)
#*{'nome': 'novo valor', 'sobrenome': 'Miranda', 'idade': 30}

print(p1)











