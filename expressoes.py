# a¹ = a
# a⁰ = 1
# a^-b = 1/a^b
# a^(b/c) = raiz "c" de a^b 
# a^b*a^c = a^(b+c)
# a^b/a^c = a^(b-c)
# a^b^c = a^(a*c)
# a^c*b^c = (a^c)*(b^c)
# (a/b)^c = a^c/b^c
# (a/b)^-c = (b/a)^c

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

# b = int(input('Digite b: '))
# print(b)
# c = int(input('Digite c: '))
# print(c)
