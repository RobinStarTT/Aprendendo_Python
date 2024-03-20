"""
*Higher Order Functions
*Funções de primeira classe
"""

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)


def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args): #!funcção que recebe uma função dentro de si mesma
    return funcao(*args)


v = executa(saudacao, 'Bom dia', 'nome')
print(v)

#?é possível passar funções como argumentos para outras funções e também é possível retornar funções de dentro de outras funções

"""
?Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

*Higher Order Functions - Funções que podem receber e/ou retornar outras funções

*First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

!Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

!Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""





