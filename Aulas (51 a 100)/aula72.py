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


def soma(*args): #argumentos não nomeados numa tupla
    #*args empacota o que é enviado para uma função dentro de uma tupla 
    total = 0 #!variável de acumulação
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

# soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

# numeros = 1, 2, 3, 4, 5, 6, 7, 8, 78, 10



# outra_soma = soma(*numeros) #!o asterisco faz o desempacotamento da variável numeros que seria enviada como tupla para a função
# #!*numeros desempacota uma tupla para enviar como parâmetros para a função soma
# print(outra_soma)
# #!quantidade ilimitada de argumentos não nomeados

# print(sum(numeros))
# #todo função soma que é natural do python






