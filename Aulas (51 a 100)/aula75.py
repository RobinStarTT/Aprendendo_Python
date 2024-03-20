"""
*Exercícios:
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
"""

def duplicar(x):
    x *= 2
    return x

"""
!Código do professor:
def duplicar(numero):
    return numero * 2
"""

def triplicar(x):
    x *= 3
    return x

def quadruplicar(x):
    x *= 4
    return x

duas_vezes = duplicar(2)
print(duas_vezes)

tres_vezes = triplicar(2)
print(tres_vezes)

quatro_vezes = quadruplicar(2)
print(quatro_vezes)

"""
!Código do professor:
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
"""







