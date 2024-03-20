from rich.traceback import install
install()

"""
*Introdução às funções (def) em Python
*Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
*Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico
?Por padrão, funções Python retornam None (nada)
"""
#!definindo uma função no python
# def Print():
#     print('Várias')


# Print()
#!é possível definir parâmetros nas funções
#todo padrão de nome para funções é o mesmo de variáveis: letra minúscula no início, underline para nomes compostos...
# def imprimir(a, b, c): #?a, b e c são parâmetros, que recebem valores ao longo do programa e se tornam argumentos
#     print(a, b,c)

#     ...

# imprimir(1, 2, 3)

def saudacao(nome = 'Sem nome'): #*caso nenhum valor seja passado para a função, ela imprime o valor padrão que lhe foi atribuído
    print(f'Olá, {nome}!')

saudacao('Lucas')

#!caso eu passe algo vazio para a função, um erro será retornado
saudacao() #?saudacao() missing 1 required positional argument: 'nome'








