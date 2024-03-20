#Exercício - sistema de perguntas e respostas

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
contador = 0
contador_de_perguntas = 0

while contador < len(perguntas):
    dicionario = perguntas[contador]
    titulo_pergunta = list(dicionario.keys())[0] #'Pergunta'
    pergunta_dicionario = dicionario[titulo_pergunta] #'Quanto é 2+2'

    print(titulo_pergunta,':', pergunta_dicionario,'\n') #Pergunta : Quanto é 2+2?

    titulo_opcoes = list(dicionario.keys())[1] #'Opções
    valores_opcoes = perguntas[contador]['Opções'] #'1', '3', '4', '5'
    indices_respostas = 0
    print('Opções:')
    for indice, opcoes in enumerate(valores_opcoes):
        print(f'{indice}) {opcoes}')
        indices_respostas += 1

    opcao_usuario = int(input('Escolha uma opção: '))
    if 0 <= opcao_usuario < len(valores_opcoes):
        titulo_resposta = list(dicionario.keys())[2]
        resposta_certa = dicionario[titulo_resposta]
        resposta_certa_cadastrada = valores_opcoes.index(resposta_certa)
        if opcao_usuario == resposta_certa_cadastrada:
            print('Você acertou!')
            contador_respostas_certas += 1
            print('______________________\n')
        else:
            print('Você errou!')
            print('______________________\n')
    
    contador += 1
    contador_de_perguntas +=1

print (f'Você acertou {contador_respostas_certas} de {contador_de_perguntas} perguntas.')