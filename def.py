def exibirMensagem():
    print('ola eu sou o python')


exibirMensagem()

def exibirMensagemPlus(mensagem):
    print('ola eu sou o python ' + mensagem)


exibirMensagemPlus("aue")


def multiplicar(numero1, numero2):
    valor = numero1 * numero2
    return valor


retorno = multiplicar(4,2)
print(retorno)

def acenderFarol():
    return "farol aceso"

print(acenderFarol())