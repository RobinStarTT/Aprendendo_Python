from rich.traceback import install
install()

# ! (Alerta) 
# ? (Dúvida) 
# TODO (Comentário) 
# * Highlight 


#* Introdução ao desempacotamento + tuplas (tuples)
#* Desempacotar é criar variáveis com os dados de dentro das listas.
#* nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']


# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes #* Aqui, na ordem da lista, foram criadas variáveis com os dados que estavam localizados dentro da lista.
# print(nome2)


# nome1, *_ = ['Maria', 'Helena', 'Luiz']
# print(nome1)


_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
