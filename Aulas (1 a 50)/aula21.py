# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor


# entrada = input('[E]ntrar [S]air: ')
# if entrada == 'E':
#     senha_digitada = input('Senha: ')
#     senha_permitida = '123456'
#     if senha_digitada == senha_permitida:
#         print('Você entrou no sistema.')
# elif entrada == 'S':
#     print('Você saiu do sistema.')
# else: 
#     print('A letra digitada não corresponde a nenhuma opção.')


# Avaliação de curto circuito
# print(True and False and True)
# print(True and 0 and True)


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
