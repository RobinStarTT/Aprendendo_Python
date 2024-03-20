import decimal
from rich.traceback import install
install()

#*Imprecisão de ponto flutuante.
#todo Double-precision floating-point format IEEE 754
#todo https://en.wikipedia.org/wiki/Double-precision_floating-point_format
#todo https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

# numero_1 = 0.1
# numero_2 = 0.7

# numero_3 = numero_1 + numero_2

# print(numero_3) #*resultado 0.79999999 (o esperado era 0.80)
# print(f'{numero_3:.2f}') #* usando a formatação o resultado é conforme o esperado (0.80)

# print(round(numero_3, 2)) #*round apenas arredonda, e não mostra os outros zeros a direita
# #!format: 0.80 (float)
# #!round: 0.8 (float)

# #todo outra forma de ter o mesmo resultado é usando o import decimal


# numero_1 = decimal.Decimal(0.1)
# numero_2 = decimal.Decimal(0.70)
# numero_3 = numero_1 + numero_2

# print(numero_3)

#* o resultado é 0.7999999999999999611421941381 - ainda mais estranho que o outro
#* então o correto é passar o valor usando o método decimal através de strings, ou seja:
#todo o método decimal é o mais indicado quando se necessita de um valor MUITO exato.

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.70')
numero_3 = numero_1 + numero_2

print(numero_3)

#!há uma imprecisão de dados por causa do tipo de dado float usado pelo python, em outras linguagens coisas semelhantes acontecem.