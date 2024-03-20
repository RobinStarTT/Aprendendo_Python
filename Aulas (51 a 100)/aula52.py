from rich.traceback import install 
install()

#* Tipo tupla - Uma lista imutável

# nomes = ['Maria', 'Helena', 'Luiz']
# nomes[1] = 'outro nome'
# _, _, nome, *resto = nomes

# print(nomes)
# print(nome)


# nomes = ['Maria', 'Helena', 'Luiz']
# quantidade_de_elementos = len(nome)

# print('Números de elementos na lsita: ', quantidade_de_elementos)

#* Para criar uma tupla, basta remover os colchetes:
#! nomes = 'Maria', 'Helena', 'Luiz'
#* ou
#! nomes = ('Maria', 'Helena', 'Luiz') - adicionar parênteses

nomes = 'Maria', 'Helena', 'Luiz'

print(nomes[-1])
print(nomes)

#* converter uma lista para uma tupla:

names = ['Maria', 'Helena', 'Luiz']

#! tuple(nome da lista)
nomes_tupla = tuple(names)

print(nomes_tupla)
