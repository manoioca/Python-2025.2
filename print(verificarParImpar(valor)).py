def verificarParImpar(numero):
    if (numero % 2 == 0):
        return 'par'
    else:
        return 'impar'


valor = int(input('digite um numero '))

print(verificarParImpar(valor))