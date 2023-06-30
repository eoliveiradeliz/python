x = float(input('Digite o valor de x:'))

y = 2*x+3

print('O valor de y é:', y)

# CORPO DE REPETIÇÃO:

if __name__ == '__main__':

    while True:

        x = int(input('Digite o valor de x:'))

        y = 2*x+3

        print('O valor de y é:', y)

        continuar = input('\nDigite [s] para sair ou [enter] para continuar:')

        if (continuar == 's'):
            break
