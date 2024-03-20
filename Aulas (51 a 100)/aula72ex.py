from rich.traceback import install
install()

"""
*Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.

*Crie uma função que diz se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero 
    return total

multiplicacao_input = multiplicacao(1, 2, 3, 4, 5)
print(multiplicacao_input)
# print(1 * 2 * 3 * 4 * 5)

def par_impar(x):
    y = ''
    if x % 2 == 0:
        y = print(f'O número {x} é par.')
    else:
        y = print(f'O número {x} é ímpar.') #!não é comum usar print em funções 
    return y

impar_input = par_impar(2)








