"""
Valores padrão para parâmetros
Ao definir um afunção, os parâmetros podemo ter valores padrão. 
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
*Refatorar: editar o seu código
"""

def soma(x, y, z = 0):
    if z: #!caso o argumento Z seja passado
        print(f'{x=} {y=} {z=}', x + y + z)

    else:
        print(f'{x=} {y=}', x + y)



soma(1, 2)
soma(3, 5, 0)
soma(100, 200, 500)

#*Verificar se um argumento foi passado ou não para um parâmetro usando o None

def soma_soma(x, y, z=None): #* todo parâmetro que vier após outro parâmetro com valor padrão, deve também ter um valor padrão
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma_soma(1, 2)
soma_soma(3, 5, 0)
soma_soma(100, 200, 500)







