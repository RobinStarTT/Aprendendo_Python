from rich.traceback import install
install()
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
"""
cpf = '121.341.670-17'
cpf_limpo = cpf.replace('.', '').replace('-', '') #!retirar os pontos e o traço do cpf
print(cpf_limpo)
nove_primeiros_digitos = cpf_limpo[:9] #!extraindo os 9 primeiros digitos do cpf em formato string, onde farei a verificação

contador = 10

resultado_primeiro_digito = 0

for digito_1 in nove_primeiros_digitos:
    resultado_primeiro_digito += int(digito_1) * contador
    contador -= 1

digito_1 = (resultado_primeiro_digito * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
"""

cpf = '442.457.951-40'
print(cpf)

cpf_limpo = cpf.replace('.', '').replace('-', '')
print(cpf_limpo)

nove_primeiros_digitos = cpf_limpo[:9]
print(nove_primeiros_digitos)

contador = 10
resultado_primeiro_digito = 0

for digito_1 in nove_primeiros_digitos:
    resultado_primeiro_digito += int(digito_1) * contador
    contador -= 1

digito_1 = (resultado_primeiro_digito * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print('O dígito 1 após o traço é: ',digito_1)





