from rich.traceback import install
install()

#* operação ternária (condicional de uma linha)
#* <valor> if <condicao> else <outro valor>


#!print('Valor' if False else 'Outro Valor')
#!print('Valor' if True else 'Outro Valor')

# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro Valor'
# print(variavel)

# digito = 9 #!validação de um dígito, se o dígito é menor ou igual a nove ele permanece com o valor normal, caso contrário, se torna 0
# # novo_digito = digito if digito <= 9 else 0
# #*agora utilizando a operação ternária:
# novo_digito_ternaria = 0 if digito > 9 else digito
# print(novo_digito_ternaria)

print('Valor' if True else 'Outro Valor' if True else 'Fim')
print('Valor' if False else 'Outro Valor' if False else 'Fim')
