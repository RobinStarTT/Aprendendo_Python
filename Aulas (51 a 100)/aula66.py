from rich.traceback import install
install()

"""
*Argumentos nomeados e não nomeados em funções Python
*Argumento nomeado tem nome com sinal de igual
*Argumento não nomeado recebe apenas o argumento (valor) 
"""


# def soma(x, y):
#     #Definição
#     print(x + y)

# #print(soma(1, 2)) #todo print nesta linha e print na função
# #*resultado: 
# #!3
# #!None O resultado da execução é None porque a função soma não retorna explicitamente um valor. 
# #?Se você quiser que a função retorne a soma em vez de apenas imprimi-la, você deve usar a palavra-chave return dentro da função

# soma(1, 2) #todo 1 e 2 são os argumentos que irão ser recebidos pelos parâmetros
# #*argumentos posicionais - dependem da ordem

def soma_soma(x, y):
    #Definição
    print(f'{x=} + {y=}', '|', 'x + y =', x + y)
#todo soma_soma é o nome da função
    #todo (1,2) é a execução da função
soma_soma(1, 2) 
soma_soma(2, 1)
soma_soma(y=2, x=1)

print(1,2, sep='-')
