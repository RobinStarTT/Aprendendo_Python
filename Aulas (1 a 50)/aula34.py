"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    
    if nome != 'sair':
        print(f'Seu nome é {nome}')
    
    else:
        break

print('Acabou')