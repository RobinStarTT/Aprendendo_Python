"""
Closure e funções que retornam outras funções
closure é uma função que retém o ambiente léxico em que foi definida. 
Isso significa que uma função dentro de outra função pode capturar variáveis locais e 
globais da função externa, mesmo após a execução da função externa ter sido concluída. Essas variáveis são então "fechadas" (capturadas) pelo closure, permitindo que a função interna acesse e manipule essas variáveis mesmo após a função externa ter retornado.
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia' )
falar_boa_noite = criar_saudacao('Boa noite')


for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))








