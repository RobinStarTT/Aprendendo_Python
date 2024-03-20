"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def duplicacoes_em_listas (lista_de_listas_de_inteiros): #define uma função chamada duplicacoes_em_listas que aceita uma lista de listas como argumento.
    for indice, lista in enumerate(lista_de_listas_de_inteiros, start=1): #loop for que itera sobre a lista de listas. A função enumerate é usada para obter tanto o índice da lista 
        #atual quanto a própria lista. O parâmetro start=1 especifica que o índice inicial será 1 (em vez do padrão 0).
        numeros_vistos = set() #criando um conjunto vazio chamado numeros_vistos para armazenar os números que já vimos na lista atual.
        primeira_duplicacao = None #Inicializamos a variável primeira_duplicacao como None. Esta variável será usada para armazenar o primeiro número duplicado encontrado na lista atual.
        for numero in lista: # loop for interno que itera sobre cada número na lista atual.
            if numero in numeros_vistos: #Esta linha verifica se o número atual já foi visto na lista atual.
                primeira_duplicacao = numero #Se o número já foi visto, atribuímos o valor desse número à variável 
                break #break interrompe o loop interno assim que a primeira duplicação é encontrada.
            numeros_vistos.add(numero) #Se o número atual não foi visto antes, adicionamos o número ao conjunto numeros_vistos
        if primeira_duplicacao is not None: # verifica se encontramos alguma duplicação na lista atual.
            print(f"Na lista {indice}, a primeira duplicação é o número {primeira_duplicacao}") #Se houver uma duplicação, essa linha imprime a mensagem indicando em qual lista a duplicação 
            #foi encontrada e qual é o número duplicado.
        else: # Se não houver duplicações na lista atual, esta parte do código é executada.
            print(f"Na lista {indice}, não há duplicações.") # imprime uma mensagem indicando que não há duplicações na lista atual.
    
duplicacoes_em_listas(lista_de_listas_de_inteiros) #Esta linha chama a função duplicacoes_em_listas passando a lista_de_listas como argumento, iniciando assim o processo de busca de 
#duplicações em todas as listas dentro da lista principal.


#!código professor 
# def encontra_primeiro_duplicado(lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1

#     for numero in lista_de_inteiros:
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break

#         numeros_checados.add(numero)

#     return primeiro_duplicado


# for lista in lista_de_listas_de_inteiros:
#     print(
#         lista,
#         encontra_primeiro_duplicado(lista)
#     )



