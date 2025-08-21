nome = input('digite o nome da pessoa')
idade = int(input('digite a idade'))
sexo = input('digite o genero -masculino ou feminino')

if (sexo.upper() == "MASCULINO"):
    sexo = "M"

elif (sexo.upper() == "FEMININO"):
    sexo = "F"

else:
    sexo = "genero nao esperado"
    

if(idade >50):
    print(f"{nome} tem {idade} anos e é experiente ({sexo})")

else:
    print(f"{nome} tem {idade} anos, esta em treinamento ({sexo})")