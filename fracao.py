numeradorF1 = int(input('Digite o numerador da primeira fração: '))
denominadorF1 = int(input('Digite o denominador da primeira fração: '))
print('A fração é {}/{}.'.format(numeradorF1, denominadorF1))

numero = int(input('Digite um inteiro: '))
fracaoMista = int(denominadorF1*numero+numeradorF1)

print('Soma de fração mista: {}/{} + {} = ({}*{}+{})/{} = {}/{} = (denominador fração * numero inteiro + numerador fração) / denominador fração'
.format(numeradorF1, denominadorF1, numero, denominadorF1, numero, numeradorF1, denominadorF1, fracaoMista, denominadorF1))

numeradorF2 = int(input('Digite o numerador da segunda fração: '))
denominadorF2 = int(input('Digite o denominador da segunda fração: '))
print('A fração é {}/{}.'.format(numeradorF2, denominadorF2))

mmc = ''

print('Soma de frações: {}/{} + {}/{} = '.format(numeradorF1, denominadorF1, numeradorF2, denominadorF2))