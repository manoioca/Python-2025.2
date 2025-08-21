nome = input('digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = (nota1 + nota2)/2

if (media > 6.5):
    situaçao = "aprovado"

else:
    situaçao = "reprovado"

print(f"A média foi {media}. O aluno está {situaçao}.")