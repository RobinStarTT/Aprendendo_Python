from rich.traceback import install
install()
import re
import sys
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
    11 10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
    77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = '803.073.111-63'
print('CPF inicial: ',cpf)
cpf_limpo = cpf.replace('.', '').replace('-', '') #!chamando o replace de forma encadeada
"""
* o replace pode ser feito da seguinte forma também:
cpf = '803.073.111-63' \
    .replace('.', '')\
    .replace('.', '')\
    .repalce('.', '')
? é possível usar o módulo re (regular expression) - import re
? que tira tudo que não é número da string do cpf por exemplo
* cpf = re.sub(
*    r'[^0-9]', (tudo que não é um número é selecionado a partir desse parâmetro)
*    '',  (e será substituído por uma string vazia)
*    '803.073.sdfsssdfjdijnfginidfn???fidnifndsijf111-63')  
!resultado do print(cpf) = 80307311163

todo entrada = input('CPF: ')
* cpf = re.sub(
*    r'[^0-9]', (tudo que não é um número é selecionado a partir desse parâmetro)
*    '',  (e será substituído por uma string vazia)
*    entrada

todo verificar se os caracteres enviados pelo usuário não são iguais ex: 11111111111

entrada_e_sequencial = entrada == entrada[0] * len(entrada)
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.)
    sys.exit()


todo o python tem outro módulo chamado sys, que contém o 'exit' que é um método que fecha o python
todo import sys


"""

# print(cpf_limpo)
cpf_nove_primeiros_digitos = cpf_limpo[:9]
# print(cpf_nove_primeiros_digitos)

contador = 10
resultado_primeiro_digito = 0

for digito_1 in cpf_nove_primeiros_digitos:
    resultado_primeiro_digito += int(digito_1) * contador
    contador -= 1

digito_1 = (resultado_primeiro_digito*10)%11
digito_1 = digito_1 if digito_1 <= 9 else 0
print('O dígito 1 após o traço é: ',digito_1)


cpf_dez_primeiros_digitos = cpf_nove_primeiros_digitos + str(digito_1)
# print(cpf_dez_primeiros_digitos)

contador = 11
resultado_segundo_digito = 0

for digito_2 in cpf_dez_primeiros_digitos:
    resultado_segundo_digito += int(digito_2) * contador
    contador -= 1
digito_2 = (resultado_segundo_digito*10)%11
digito_2 = digito_2 if digito_2 <=9 else 0
print('O dígito 2 após o traço é: ', digito_2)

cpf_final = cpf_dez_primeiros_digitos+str(digito_2)
cpf_final_formatado = f"{cpf_final[:3]}.{cpf_final[3:6]}.{cpf_final[6:9]}-{cpf_final[9:]}"
print('O CPF completo equivale a: ', cpf_final_formatado)

if cpf == cpf_final_formatado:
    print('CPF válido')

else:
    print('CPF Inválido')


