print('Propriedades Exponenciação/Potenciação\n\nP1: a¹ = a, P2: a⁰ = 1\n')
a = int(input('Digite a: '))
print(a)

for expoente in range(4):
    if expoente == 0:
        print('a⁰ = {}'.format(a**expoente))
    if expoente == 1:
        print('a¹ = {}'.format(a**expoente))
    if expoente == 2:
        print('a² = {}'.format(a**expoente))
    if expoente == 3:
        print('a³ = {}'.format(a**expoente))

print('\nP3: a**(-b) = 1/a**b')
b = int(input('Digite b: '))
print(b)

print('a**-b = {} = 1/{}'.format(a**-b, a**b))

print('\nP4: a**(b/c)\n= raiz de índice "c", de base "a", expoente "b"')
c = int(input('Digite c: '))
print(c)
print('{}**{}/{} = {}**{}'.format(a, b, c, a, b/c))
print('O índice (c) na radiciação é o denominador do expoente fracionário na exponenciação em R* \nA base (a) na radiciação é a base da exponenciação.\nO expoente (b) da radiciação é o numerador da exponenciação fracionária dividido pelo índice da radiciação (b/c). \nOu seja, quando se eleva um número Z por uma fração obtém-se a raíz do número inteiro.')
# print('a**(b/c) = {:.3f}'.format(a**(b/c))); output: 1.260 para imput a=2, b=1, c=3;
print('a**(b/c) = {}'.format(a**(b/c))) # output: 1.2599210498948732

# a^b*a^c = a^(b+c)
print('\nP5: (a**b)*(a**c) = a**(b+c)')
print('({}**{})*({}**{}) = {} = '.format(a, b, a, c, a**b*a**c))
print('{}**({}+{}) = {} = '.format(a, b, c, a**(b+c)))

# a^b/a^c = a^(b-c)
print('\nP6: a**b/a**c = a**(b-c)')
print('{}**{}/{}**{} = {}'.format(a, b, a, c, a**b/a**c))
print('{}**({}-{}) = {}'.format(a, b, c, a**(b-c)))

# (a^b)^c = a^(a*c)
print('\nP7: (a**b)**c = a**(b*c)')
print('({}**{})**{} = {}'.format(a, b, c, (a**b)**c))
print('{}**({}*{}) = {}'.format(a, b, c, a**(b*c)))

# a^c*b^c = (a^c)*(b^c)
print('\nP8: a**b*b**c = (a**b)*(b**c)')
print('({}**{})*({}**{}) = {}'.format(a, b, b, c, a**b*b**c))

# (a/b)^c = a^c/b^c
print('\nP9: (a/b)**c = a**c/b**c')
print('({}/{})**{} = {}'.format(a, b, c, (a/b)**c))

# (a/b)^-c = (b/a)^c
print('\nP10: (a/b)**(-c) = (b/a)**c')
print('({}/{})**{} = {}/{}**{} = {}'.format(a, b, -c, b, a, c, (a/b)**(-c)))
print((b/a)**c)
