a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
mdc = 0

if a < b:
    a, b = b, a

def gcd(a, b, mdc):
    while a != 0:
        a, b = b % a, a
        mdc = b
        print(a, b)
    print('mdc = {}'.format(mdc))

gcd(a, b, mdc)