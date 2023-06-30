nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('Media: ', media)

if media < 7.0:
    print('Reprovado')
elif media < 10:
    print('Aprovado')
else:
    print('Aprovado com Distinção!')
