from rich.traceback import install
install()

"""
*args - Argumentos não nomeados
* - * args (empacotamento e desempacotamento)
"""

#!desempacotamento:
# x, y, *resto = 1, 2, 3, 4 #?tupla
# print(x, y, resto)
# #todo empacotamento acontece quando a variável resto absorve os valores 3 e 4
# #todo desempacotamento acontece quando as variáveis x e y recebem os valores 1 e 2


# def soma(x, y):
#     return x + y


def soma(*args): #argumentos não nomeados
    total = 0 #!variável de acumulação
    for numero in args:
        total += numero
        print(numero)
    print(total)

soma(1, 2, 3, 4, 5, 6)

# print(1, 2, 3, 4, 5)


