"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 100, 2)
vzs_laco = 0
for numero in numeros:
    print(numero)
    vzs_laco += 1
print('Quantidade de vezes que o lçao foi repetido: ',vzs_laco)
