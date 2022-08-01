operação = int(input(''
                     'Qual operação desejada ? \n'
                    '1 para somar \n'
                    '2 para multiplicar\n'
                    '3 para dividir\n'
                    '4 para potenciação\n'))


numero_1 = float(input('Insira o primeiro numero: \n'))
numero_2 = float(input('Insira o segundo numero: \n'))

if operação == 1:
    print(numero_1 + numero_2)
elif operação == 2:
    print(numero_1 * numero_2)
elif operação == 2:
    print(numero_1 / numero_2)
else:
    print(numero_1 ** numero_2)
