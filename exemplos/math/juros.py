import math


def simples():
    investimento = float((input('\n\nInvestimento Inicial:')))
    tjurospercentagem = float((input('Taxa de Juros (em %) :')))
    tjuro = tjurospercentagem/100
    anos = int(input('Anos:'))
    varfuturo = investimento*(1+tjuro*anos)
    jurototal = investimento*tjuro*anos
    juroano = investimento*tjuro
    print('\n\n\t\t O valor futuro é de {:.2f}'.format(varfuturo))
    print('\n\t\t Os juros totais é de {:.2f}'.format(jurototal))
    print('\n\t\t Os juros ao ano é de {:.2f}'.format(juroano))


def composto():
    investimento1 = float((input('\n\nInvestimento Inicial:')))
    tjurospercentagem1 = float((input('Taxa de Juros (em %) :')))
    tjuro1 = tjurospercentagem1/100
    anos1 = int(input('Anos:'))
    varfuturo1 = investimento1*pow(1+tjuro1, 3)
    jurototal1 = investimento1*(pow(1+tjuro1, 3)-1)
    print('\n\n\t\t O valor futuro é de {:.2f}'.format(varfuturo1))
    print('\n\t\t Os juros totais é de {:.2f}'.format(jurototal1))


def menu():
    while True:
        try:
            menu5 = ' |[1] Juros Simples   |'
            menu1 = ' |[2] Juros Compostos |'
            menu2 = ' |[3] Sair            |'
            menu3 = '---------------------'
            print('\n\n')
            print(menu3.center(80, ' '))
            print(menu5.center(80, ' '))
            print(menu1.center(80, ' '))
            print(menu2.center(80, ' '))
            print(menu3.center(80, ' '))
            option = int(input(' Escolha a opção: '))
            if option == 1:
                simples()
                menu()
            elif option == 2:
                composto()
                menu()
            elif option == 3:
                print('Fim do Programa')
                exit()
            else:
                print('Escolha Inválida. Escolha entre 1 a 3')
        except ValueError:
            print('Escolha Inválida. Escolha entre 1 a 3')


menu()
