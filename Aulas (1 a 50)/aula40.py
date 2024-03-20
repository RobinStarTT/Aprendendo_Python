# '''Calculadora com while'''

# operacao = input('Digite o símbolo da operação que você quer realizar (+ = soma; - = subtração; * = multiplicação; / = divisão) e para sair digite (s): ')

# while operacao != 's':

#     if operacao in ['+', '-', '*', '/']: 
#         numero_1 = float(input('Digite o primeiro número: '))
#         numero_2 = float(input('Digite o segundo número: '))

#         if operacao == '+':
#             resultado = numero_1 + numero_2
#             print(f'O resultado da soma dos números {numero_1} + {numero_2} foi: {resultado}')

#         elif operacao == '-':
#             resultado = numero_1- numero_2
#             print(f'O resultado da subtração dos números {numero_1} - {numero_2} foi: {resultado}')

#         elif operacao == '*':
#             resultado = numero_1 * numero_2
#             print(f'O resultado da multiplicação dos números {numero_1} * {numero_2} foi: {resultado}')
        
#         elif operacao == '/':
#             if numero_2 != 0:
#                 resultado = numero_1 / numero_2
#                 print(f'O resultado da divisão dos números {numero_1} / {numero_2} foi: {resultado}')
#             else:
#                 print('Não é possível divisão por zero.')
#     else:
#         print('Operação inválida.')

#     operacao = input('Digite o símbolo da operação que você quer realizar (+ = soma; - = subtração; * = multiplicação; / = divisão) e para sair digite (s): ')
# print('Você saiu do programa.')


""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break