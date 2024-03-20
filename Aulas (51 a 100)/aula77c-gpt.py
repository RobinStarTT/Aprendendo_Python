perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador_respostas_certas = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])

    # Imprimindo as opções
    for indice_opcao, opcao in enumerate(pergunta['Opções']):
        print(f'{indice_opcao}) {opcao}')

    opcao_usuario = int(input('Escolha uma opção: '))

    # Verifica se a opção escolhida pelo usuário é válida
    if 0 <= opcao_usuario < len(pergunta['Opções']):
        resposta_correta = pergunta['Resposta']
        resposta_usuario = pergunta['Opções'][opcao_usuario]

        # Comparando a resposta do usuário com a resposta correta
        if resposta_usuario == resposta_correta:
            print('Você acertou!')
            contador_respostas_certas += 1
        else:
            print('Você errou!')
    else:
        print('Opção inválida!')

    print('______________________\n')

print(f'Você acertou {contador_respostas_certas} de {len(perguntas)} perguntas.')
