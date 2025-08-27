def verificarParImpar(numero):
    if (numero % 2 == 0):
        return True
    else:
        return False


valor = int(input('digite um numero '))

if(verificarParImpar(valor)):
    print('O numero é par')
else:
    print('o numero é impar')