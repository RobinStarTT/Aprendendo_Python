import os 
from rich.traceback import install
install()

#* Faça uma lista de compras com listas, o usuário deve ter a possibilidade de inserir, apagar e listar valores
#* da sua lista. Não permita que o programa quebre com erros de índices inexistentes na lista.

lista_compras = []

while True:
    opcao = input('Selecione uma opção!\n[i]nserir [a]pagar [l]istar [s]air: ').lower() #*.lower serve para que tudo que o usuário for digitar, seja formatado para minúsculo
    if opcao == 'i':
        valor_item = input('Valor: ')
        lista_compras.append(valor_item)

    elif opcao == 'a':
        indice_apagar = input('Escolha o índice para apagar: ')
        try:
            indice_apagar = int(indice_apagar)
            if 0 <= indice_apagar < len(lista_compras):
                item_removido = lista_compras.pop(indice_apagar)
                print(f'O item {item_removido} foi removido da lista!')
            else:
                print(f'O item de índice {indice_apagar} não está na lista!')
        except ValueError:  #*poderia adicionar um IndexError para contornar o erro no índice. Mas o else acima já revisa esse tópico.
            print('Insira um índice válido.')
        #! É possível usar mais de um except no mesmo try. Por exemplo:
        #*except IndexError ou except TypeError
            

    elif opcao == 'l':
        if not lista_compras:
            print('Nada para listar.')
        else:
            for indice, item in enumerate(lista_compras):
                print(indice, item)
    
    elif opcao == 's':
        print('Saindo do programa.')
        break

    else:
        print('Opção selecionada inválida.')

