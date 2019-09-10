#Aqui é o menu
menu = 'sim'
while menu == 'sim':
    print('\n|--------------------------------|'
          '\n|digite a opção de calculo:      |'
          '\n|(1)Calcular bhaskara            |'
          '\n|(2)Calcular a Area do Trapezio  |'
          '\n|(3)Calcular a Area do Triangulo |'
          '\n|(4)Calcular a Area do Quadrado  |'
          '\n|          ou Quadrado           |'
          '\n|se deseja sair digitar "sair"   |'
          '\n|--------------------------------|'
          '\n')
    opcao = input('opcão: ')
    if opcao == '1':

        print('\n|------------------------------|'
              '\n|Calculo da formula de Bhaskara|'
              '\n|------------------------------|\n\n')

        # valor de a,b e c
        a = float(input('Colocar o valor de a: '))
        b = float(input('Colocar o valor de b: '))
        c = float(input('Colocar o valor de c: '))

        # calculo para achar o valor de delta
        delta = b ** 2 - 4 * a * c

        # observa se o valor de "delta" é igual ou menor que "zero" se ele não for
        # ele continua a conta
        if delta <= 0:
            print('\nDelta =', delta, '\n\nNão existe raiz!')
        else:
            # "xp" é equivalente a x' e "xn" é x"
            xp = ((-b) + delta ** 0.5) / (2 * a)
            xn = ((-b) - delta ** 0.5) / (2 * a)
            print('\nO valor de delta é {}\n'
                  '\nOs valore de x¹ e x² é:\nx¹={}\nx²={}'.format(delta, xp, xn))
        menu = input('\n'
                     '\nDeseja continuar?'
                     '\n  sim ou nao:\n   ')


    elif opcao == '2':

        print('\n|----------------|'
              '\n|Area do trapezio|'
              '\n|----------------|\n')

        B = float(input('Coloque o valor da Base Maior: '))
        b = float(input('Coloque o valor da base menor: '))
        h = float(input('Coloque o valor da Altura: '))

        area = ((B + b) * h) / 2

        print('\nO valor da area do trapezio é:\n   {}'.format(area))

        menu = input('\n'
                     '\nDeseja continuar?'
                     '\n   sim ou nao:\n    ')

    elif opcao == '3':

        print('\n|-----------------|'
              '\n|Area do triangulo|'
              '\n|-----------------|\n')

        b = float(input('Coloque o valor da base do triangulo: '))
        h = float(input('Coloque o valor da altura do triangulo: '))

        area = (b * h) / 2

        print('\nO valor da Area do Triangulo é:\n   {}'.format(area))

        menu = input('\n'
                     '\nDeseja continuar?'
                     '\n   sim ou nao:\n   ')

    elif opcao == '4':

        print('\n|-----------------|'
              '\n|Area do Retangulo|'
              '\n|       ou        |'
              '\n|    Quadrado     |'
              '\n|-----------------|\n')

        b = float(input('Coloque o valor da base do retangulo ou quadrado: '))
        h = float(input('Coloque o valor da altura do retangulo ou quadrado: '))

        # area = b*h
        if b == h:
            areaQ = b * h
            print('\nA Area do quadrado é:\n{:12}'.format(areaQ))
        else:
            area = b * h
            print('\nA Area do retangulo é:\n    {}'.format(area))

        menu = input('\n'
                     '\nDeseja continuar?'
                     '\n   sim ou nao:\n   ')

    elif opcao == 'sair':
        menu = 'nao'
    else:
        print('\n|¨¨¨¨¨¨¨¨¨|                  |¨¨¨¨¨¨¨¨¨¨|'
              '\n|  |¨¨¨¨| |                  |  |¨¨¨¨¨| |'
              '\n|  |    | |                  |  |     | |' 
              '\n|  |    | |                  |  |     | |'
              '\n|  |____| |   |¨¨¨¨¨¨¨¨¨¨¨|  |  |_____| |'
              '\n|_________|   |___________|  |__________|'
              '\n'
              '\nMar que merda é essa?')
        input('\nPressione "enter"')

