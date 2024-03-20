# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

print(int('1') + 1)

print('b' + '11')

print('a' + 'b')



"""
Como o python tem a tipagem forte e dinâmica, ele reconhece que está sendo usado números ou letras e decide o que acontece quando se usa o sinal de soma.
Em números ele soma, resultando num número maior.
Em letras ele concatena, resultando numa sílada, ou palavra.
"""
