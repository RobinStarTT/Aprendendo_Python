from rich.traceback import install
install()

"""
Retorno de valores das funções (return)
"""
# variavel = print('Luiz')
# #*resultado é Luiz

# print(variavel)
# #*resultado é None

# #?None significa um 'não valor'
# #!variavel = print('Luiz')

# variavel = None
# print(variavel is None)

def soma(x , y):
    print('Olha só que legal')
    if x > 10:
        return 10, 20 #*pode enviar uma lista, uma tupla, o que for necessário
    return x + y #!a palavra return diz que a função retornará de forma otimizada esse valor do cálculo
    print(1+1) #!essa parte do código é inalcançável, ou seja, tudo que é feito após o return, é desconsiderado pelo python
#*somente funções e métodos tem a palavra return

# variavel = soma(1,2)
# variavel = int('1')

# print(variavel)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
# print(soma1 + soma2)
#?unsupported operand type(s) for +: 'NoneType' and 'NoneType'
#*a função soma não RETORNA nada

print(soma(11, 55))




