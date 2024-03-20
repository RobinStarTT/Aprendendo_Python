"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um número inteiro: ')
# numero_tipo = numero.isdecimal()

# if not numero_tipo:
#     print(f'O número digitado {numero} não é inteiro.')
    
# else:
#     numero_conv_int = int(numero)
#     if numero_conv_int % 2 == 0:
#         print(f'O número digitado {numero} é par.')
#     else:
#         print(f'O número digitado {numero} é ímpar.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Digite a hora (somente hora): ')
# hora_conv = int(hora)

# if hora_conv >= 0 and hora_conv <=11:
#     print(f'A hora digitada foi {hora_conv}. Bom dia!')

# elif hora_conv >= 12 and hora_conv <= 17:
#     print(f'A hora digitada foi {hora_conv}. Boa tarde!')

# elif hora_conv >=18 and hora_conv <= 23:
#     print(f'A hora digitada foi {hora_conv}. Boa noite!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)
if tamanho_nome <= 4 and tamanho_nome > 1:
    print(f'O nome digitado foi {nome} e ele é curto.')

elif tamanho_nome >= 5 and tamanho_nome <=6:
    print(f'O nome digitado foi {nome} e ele é normal.')

elif tamanho_nome > 6:
    print(f'O nome digitado foi {nome} e ele é muito grande.')

else:
    print(f'Nenhum nome foi digitado: {nome}.')